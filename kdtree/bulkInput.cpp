//
//  bulkInput.cpp
//  KDtree
//
//  Created by Deepanker Mishra on 27/03/18.
//  Copyright © 2018 Deepanker Mishra. All rights reserved.
//

#include "bulkInput.hpp"

using namespace std;

pair<unsigned int, vector<Point> > readFile(char* filename){
    ifstream fin(filename);
    int dim, numlines, i;
    double dub;
    fin >> dim >> numlines;
    vector<Point> allPoints;
    while(numlines--){
        i=dim;
        Point inp;    
        while(i--){
            fin >> dub;
            inp.push_back(dub);
        }
        allPoints.push_back(inp);
    }
    return pair<unsigned int, std::vector<Point> >(dim, allPoints);
}

Point readQuery(char* queryfile){
    ifstream fin(queryfile);
    int dim;
    fin >> dim;
    Point query;
    double val;
    while(dim--){
        fin >> val;
        query.push_back(val);
    }
    return query;
}

int partition(vector<Point>& v, int l, int h, int dim){
    assert(h>=l);
    int med = l;
    Point pivpoint = v[h];
    for(int i=l;i<h;i++){
        if(v[i][dim]<=pivpoint[dim]){
            Point temp = v[i];
            v[i] = v[med];
            v[med] = temp;
            med++;
        }
    }
    v[h] = v[med];
    v[med] = pivpoint;
    return med;
}

int median(vector<Point>& vp, int k, int l, int h, int dim){
//    cerr<<"l: "<<l<<" h: "<<h<<" k: "<<k<<endl;
    assert(h>=l);
    if(h==l)return l;
    int pos = partition(vp,l,h,dim);
//    cerr<<"pos: "<<pos<<endl;
    if(pos-l == k) return pos;
    else if(pos-l<k) return median(vp, k-pos+l-1, pos+1, h, dim);
    return median(vp, k, l, pos-1, dim);
}

void makeKDTree(vector<Point>& vp, int l, int h, int curdim, int totaldim, KDTree& kdt){
    if(l>h)return;
    int mid = (h-l+1)>>1;
    int med = median(vp, mid, l, h, curdim);
    kdt.insert(vp[med]);
    // cerr<<"med is inserted: "<<med<<endl;
    // cerr<<"make left tree"<<endl;
    makeKDTree(vp, l, med-1, (curdim+1)%totaldim, totaldim, kdt);
    // cerr<<"make right tree"<<endl;
    makeKDTree(vp, med+1, h, (curdim+1)%totaldim, totaldim, kdt);
}

KDTree bulkInsert(char* filename, KDTree& kdt){
    // cerr << "begin"<<endl;
    pair<unsigned int, vector<Point> > allPoints = readFile(filename);
    // cerr << "end"<<endl;
    kdt.dim = allPoints.first;
    makeKDTree(allPoints.second, 0, allPoints.second.size() - 1, 0, allPoints.first, kdt);
    return kdt;
}

