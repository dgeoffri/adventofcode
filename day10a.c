#include <stdio.h>
#include <string.h>

#define XMAX  128
#define YMAX  128
#define NUMPOINTS 334

struct Rect {
	int	width;
	int	height;
};

struct Point {
	int		x;
	int		y;
	int	xvelocity;
	int	yvelocity;
};

void marchPoints(struct Point *pointlist) {
	int		i;
	for (i=0; i<NUMPOINTS; i++) {
		pointlist[i].x += pointlist[i].xvelocity;
		pointlist[i].y += pointlist[i].yvelocity;
	}
}

struct Rect findArea(struct Point *pointlist) {
	int xmin;
	int ymin;
	int xmax;
	int ymax;
	struct Rect r;
	int i;
	xmin = xmax = pointlist[0].x;
	ymin = ymax = pointlist[0].y;
	for (i=1; i<NUMPOINTS; i++) {
		if (pointlist[i].x < xmin)
			xmin = pointlist[i].x;
		if (pointlist[i].y < ymin) 
			ymin = pointlist[i].y;
		if (pointlist[i].x > xmax)
			xmax = pointlist[i].x;
		if (pointlist[i].y > ymax)
			ymax = pointlist[i].y;
	}
	// printf ("  xmin: %d, ymin: %d, xmax: %d, ymax: %d  xmax-xmin: %d  ymax-ymin: %d\n", xmin, ymin, xmax, ymax, xmax-xmin, ymax-ymin);
	r.width=xmax-xmin;
	r.height=ymax-ymin;
	return r;
}

struct Point findOrigin(struct Point *pointlist) {
	struct Point p;
	int i;
	p.x	= pointlist[0].x;
	p.y	= pointlist[0].y;
	for (i=1; i<NUMPOINTS; i++) {
		if (pointlist[i].x < p.x)
			p.x = pointlist[i].x;
		if (pointlist[i].y < p.y) 
			p.y = pointlist[i].y;
	}
	return p;
}

void saveGrid(int grid[XMAX][YMAX], int i) {
	FILE *outfile;
	char fn[128];
	int  x, y;
	snprintf (fn, sizeof(fn), "day10a-frame%08d.pbm", i);
	outfile = fopen(fn, "w");
	fprintf (outfile, "P1\n%d\n%d\n", XMAX, YMAX);
		for (y=0; y<YMAX; y++) {
			for (x=0; x<XMAX; x++) {
				fprintf(outfile, "%d ", grid[x][y] ? 0 : 1);
		}
		fprintf(outfile, "\n");
	}
	fclose(outfile);
	printf ("  Saved iteration %d as %s\n", i, fn);
}

int main(int argc, char **argv) {
	FILE 		*infile;
	struct Point	pointlist[NUMPOINTS];	
	int 		grid[XMAX][YMAX];
	int 		x, y, i;

	infile = fopen("day10.txt", "r");
	if (!infile) {
		printf ("Can't open file\n");
		return 1;
	}
	for (i=0; i<NUMPOINTS; i++) 
		fscanf (infile, "position=<%d,  %d> velocity=<%d, %d>\n", &(pointlist[i]).x, &(pointlist[i]).y, &pointlist[i].xvelocity, &pointlist[i].yvelocity);
	fclose (infile);
	
	for (i=0; i<20000; i++) {
		struct Rect r = findArea(pointlist);
		printf ("Iteration %d, rectangle dimensions are %dx%d\n", i, r.width, r.height);
		if ((r.width<=XMAX) && (r.height<=YMAX)) {
			struct Point origin = findOrigin(pointlist);
			int j;
			memset(grid, 0, sizeof(grid));
			for (j=0; j<NUMPOINTS; j++)
				grid[pointlist[j].x - origin.x][pointlist[j].y - origin.y] = 1;
			saveGrid(grid, i);
		}
		marchPoints(pointlist);
	}
}
