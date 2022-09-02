#include <math.h> 

#define DLLEXPORT extern "C" __declspec(dllexport)

DLLEXPORT struct Dot
{
	float x;
	float y;
};

DLLEXPORT float scalar_product(Dot p1, Dot p2) {
	return p1.x * p2.x + p1.y * p2.y;
}

DLLEXPORT float TTP(Dot p1, Dot p2, Dot p) {
	float coss;
	Dot vec1, vec2;
	vec1.x = p2.x - p1.x;
	vec1.y = p2.y - p1.y;

	vec2.x = p.x - p1.x;
	vec2.y = p.y - p1.y;
	coss = scalar_product(vec1, vec2);
	if (coss <= 0)
		return sqrt((p1.x - p.x) * (p1.x - p.x) + (p1.y - p.y) * (p1.y - p.y));
	Dot vec3;
	vec3.x = p.x - p2.x;
	vec3.y = p.y - p2.y;
	if (scalar_product(vec1, vec3) >= 0)
		return sqrt((p2.x - p.x) * (p2.x - p.x) + (p2.y - p.y) * (p2.y - p.y));
	coss /= sqrt(vec1.x * vec1.x + vec1.y * vec1.y) * sqrt(vec2.x * vec2.x + vec2.y * vec2.y);
	coss = sqrt(1 - coss * coss);
	return coss * sqrt(vec2.x * vec2.x + vec2.y * vec2.y);
}

DLLEXPORT bool same_direct(Dot p1, Dot p2, Dot d1, Dot d2) {
	Dot vec1, vec2;
	vec1.x = p2.x - p1.x;
	vec1.y = p2.y - p1.y;

	vec2.x = d2.x - d1.x;
	vec2.y = d2.y - d1.y;
	return scalar_product(vec1, vec2) / (sqrt(vec1.x * vec1.x + vec1.y * vec1.y) * sqrt(vec2.x * vec2.x + vec2.y * vec2.y)) >= sqrt(2) / 2;
}

DLLEXPORT float length(Dot* t, int size) {
	float res = 0;
	for (int i = 0; i < size - 1; i++)
		res += sqrt((t[i + 1].x - t[i].x) * (t[i + 1].x - t[i].x) + (t[i + 1].y - t[i].y) * (t[i + 1].y - t[i].y));
	return res;
}

DLLEXPORT float matches(Dot* t1, int size1, Dot* t2, int size2, float eps) {
	bool* incl = new bool[size1];
	float res1 = 0, res2 = 0;
	for (int i = 0; i < size2 - 1; i++)
		if (TTP(t2[i], t2[i + 1], t1[0]) < eps) {
			incl[0] = true;
			break;
		}
	bool t = false;
	for (int i = 1; i < size1; i++) {
		res2 += sqrt((t1[i].x - t1[i - 1].x) * (t1[i].x - t1[i - 1].x) + (t1[i].y - t1[i - 1].y) * (t1[i].y - t1[i - 1].y));
		for (int j = 0; j < size2 - 1; j++) {
			t = t || TTP(t2[j], t2[j + 1], t1[i]) < eps;
			incl[i] = TTP(t2[j], t2[j + 1], t1[i]) < eps && same_direct(t2[j], t2[j + 1], t1[i - 1], t1[i]);
			if (incl[i])
				break;
		}
		if (incl[i] && incl[i - 1])
			res1 += sqrt((t1[i].x - t1[i - 1].x) * (t1[i].x - t1[i - 1].x) + (t1[i].y - t1[i - 1].y) * (t1[i].y - t1[i - 1].y));
		incl[i] = t;
	}
	return res1 / res2;
}

DLLEXPORT float Matches_All(Dot* t1, int size1, Dot* t2, int size2, float eps) {
	float s1 = length(t1, size1), s2 = length(t2, size2);
	return (matches(t1, size1, t2, size2, eps)*s1 + matches(t2, size2, t1, size1, eps)*s2) / (s1+s2);
}