//
//  KDTree.cpp
//  KDtree
//
//  Created by Deepanker Mishra on 24/03/18.
//  Copyright © 2018 Deepanker Mishra. All rights reserved.
//

#include "KDTree.hpp"
using namespace std;

/*
 * TODO: Need to handel bounding rectangles, currently bounding rectangle is
 * same as the point it self.
 */


// not sure
void updateMinBoundary(Point& mb, Point& p){
    for(int i=0;i<mb.size();i++){
        mb[i] = min(mb[i],p[i]);
    }
}

// not sure
void updateMaxBoundary(Point& mb, Point& p){
    for(int i=0;i<mb.size();i++){
        mb[i] = max(mb[i],p[i]);
    }
}


pair<char,Node*> KDTree::insertHelper(Node* at, Point p, int d){
    if(at==NULL) return pair<char, Node*>('n', at); // n for root is null
    else if(at->point[d] >= p[d]){
        updateMinBoundary(at->minboundary, p);
        updateMaxBoundary(at->maxboundary, p);
        if(at->left==NULL) return pair<char,Node*>('l',at); // l for left child and not found
        return insertHelper(at->left, p, (d+1)%dim);
    }
    else{
        updateMinBoundary(at->minboundary, p);
        updateMaxBoundary(at->maxboundary, p);
        if(at->right==NULL) return pair<char,Node*>('r',at); // r for right child and not found
        return insertHelper(at->right, p, (d+1)%dim);
    }
}

void KDTree::insert(Point p){
    pair<char, Node*> here = insertHelper(root, p, 0);
    Node* at = here.second;
    switch (here.first) {
        case 'n':
            // first insert when root is null
            dim = (unsigned int)p.size();
            root = new Node(p);
            break;
        case 'l':
            at->left = new Node(p);
            break;
        case 'r':
            at->right = new Node(p);
            break;
        default:
            cerr<<"should not enter here"<<endl;
            break;
    }
}

void KDTree::printPoint(Point p){
    cerr<<"(";
    int i=0;
    for(;i< p.size()-1;i++){
        cerr<< p[i]<<" ";
    }
    cerr<< p[i] <<")"<<endl;
}

void KDTree::kdPrint(Node* r){
    if(r==NULL) {
        cerr<< "-x-" <<endl;
        return;
    }
    printPoint(r->point);
    cerr<<"***LEFT***"<<endl;
    kdPrint(r->left);
    cerr<<"***RIGHT***"<<endl;
    kdPrint(r->right);
}
