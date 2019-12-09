//
//  KDTree.hpp
//  KDtree
//
//  Created by Deepanker Mishra on 24/03/18.
//  Copyright © 2018 Deepanker Mishra. All rights reserved.
//

#ifndef KDTree_hpp
#define KDTree_hpp

#include <iostream>
#include<vector>
typedef std::vector<double> Point;

struct Node{
    Point point;
    
    // bounding rectangle
    Point minboundary;
    Point maxboundary;
    
    Node* left;
    Node* right;
    Node(){
        left = NULL;
        right = NULL;
    };
    Node(Point p){
        point = p;
        left = NULL;
        right = NULL;
        minboundary = p;
        maxboundary = p;
    }
};

struct KDTree{
    /* data memebers */
    unsigned int dim;
    Node* root;
    
    /* functions */
    void insert(Point p);
    Node* search(Point p);
    std::pair<char, Node*> searchHelper(Node* at, Point p, int d);
    std::pair<char, Node*> insertHelper(Node* at, Point p, int d);
    void kdPrint(Node* r);
    static void printPoint(Point p);
    KDTree(){
        root = NULL;
        dim = 0;
    }
    KDTree(unsigned int d){
        dim = d;
        root = NULL;
    }
};

#endif /* KDTree_hpp */
