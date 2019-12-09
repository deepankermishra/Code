//
//  main.cpp
//  KDtree
//
//  Created by Deepanker Mishra on 24/03/18.
//  Copyright © 2018 Deepanker Mishra. All rights reserved.
//

#include <iostream>
#include <queue>
#include <vector>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include "KDTree.hpp"
#include "bulkInput.hpp"

using namespace std;

typedef pair<double, Node*> nodeInfo; // l2 distance from query, pointer to the node

struct mincomp{
    bool operator()(const nodeInfo& i, const nodeInfo& j){
            return i.first > j.first;
        
    }
};

struct maxcomp{
    bool operator()(const nodeInfo& i, const nodeInfo& j){
        if(i.first != j.first)
            return i.first < j.first;
        else{
            for(int a=0;a<i.second->point.size();a++){
                if((i.second->point)[a] != (j.second->point)[a])
                    return (i.second->point)[a] < (j.second->point)[a];
            }
        }
        return false;
    }
};

bool leq(const Point& i, const Point& j){
	for(int a=0;a<i.size();a++){
        if(i[a] != j[a])
            return i[a] < j[a];
    }
    return false;
}

typedef priority_queue<nodeInfo, vector<nodeInfo >, mincomp > MinHeap;
typedef priority_queue<nodeInfo, vector<nodeInfo >, maxcomp > MaxHeap;

// not used
double l2(const Point& p1, const Point& p2){
    double d = 0;
    for(int i=0; i<p1.size(); i++){
        d += (p1[i]-p2[i])*(p1[i]-p2[i]);
    }
    return (d); // optional for speed up
}

double mbr(const Node* n, const Point& q){
    double val = 0;
    for(int i=0;i<q.size();i++){
        if(q[i] < n->minboundary[i]){
            val+= (q[i] - n->minboundary[i]) * (q[i] - n->minboundary[i]);
        }else if(q[i] > n->maxboundary[i]){
            val+= (q[i] - n->maxboundary[i]) * (q[i] - n->maxboundary[i]);
        }
    }
    return (val); // optional for speed up
}


vector<Point> knn(const KDTree kdt, const Point& q, const int k){
    /*
     * does only upward pruning
     */
    MaxHeap bestk;      // best K distances seen till now
    MinHeap candidate;  // heap for tranversal
    nodeInfo tempNodeInf = nodeInfo(mbr(kdt.root,q),kdt.root) ;
    candidate.push(tempNodeInf);
    while(1){
        // assert(bestk.size()<=k);
        if(candidate.empty()) break;
        nodeInfo cur = candidate.top(); candidate.pop();
        Node* curnode = cur.second;
        if(bestk.size()<k){
            tempNodeInf.first = l2(curnode->point,q);
            tempNodeInf.second = curnode;
            bestk.push(tempNodeInf);
            if(bestk.size() == k){
                // if size became k after current insert push children with pruning in candidate
                if(curnode->left){
                    double dist = mbr(curnode->left, q);
                    nodeInfo temp = bestk.top();
                    if(dist < temp.first || (dist == temp.first && leq(curnode->left->point, temp.second->point))){
                        tempNodeInf.first = dist; tempNodeInf.second = curnode->left;
                        if(curnode->left->left == NULL && curnode->left->right==NULL){
                            bestk.pop();
                            bestk.push(tempNodeInf);
                        }else{
                            candidate.push(tempNodeInf);
                        }
                    }
                }
                if(curnode->right){
                    double dist = mbr(curnode->right, q);
                    nodeInfo temp = bestk.top();
                    if(dist<temp.first || (dist == temp.first && leq(curnode->right->point, temp.second->point))){
                        tempNodeInf.first = dist; tempNodeInf.second=curnode->right;
                        if(curnode->right->left == NULL && curnode->right->right==NULL){
                            bestk.pop();
                            bestk.push(tempNodeInf);
                        }else{
                            candidate.push(tempNodeInf);
                        }
                    }
                }
            }else{
                // less than k elements seen push both the children without pruning
                if(curnode->left){
                    double dist = mbr(curnode->left, q);
                    tempNodeInf.first = dist; tempNodeInf.second = curnode->left;
                    candidate.push(tempNodeInf);
                }
                if(curnode->right){
                    double dist = mbr(curnode->right, q);
                    tempNodeInf.first = dist; tempNodeInf.second = curnode->right;
                    candidate.push(tempNodeInf);
                }
            }
        }else{
            // assert(bestk.size()==k);
            if(cur.first > bestk.top().first) break;
            else{
                // size == k push children with pruning in candidate
                double curl2 = l2(curnode->point,q);
                nodeInfo temp = bestk.top();
                if(curl2<temp.first || (curl2 == temp.first && leq(curnode->point, temp.second->point))){
                    bestk.pop();
                    bestk.push(nodeInfo(curl2,curnode));
                    temp = bestk.top();
                }
                if(curnode->left){
                    double dist = mbr(curnode->left, q);
                    if(dist < temp.first || (dist == temp.first && leq(curnode->left->point, temp.second->point))){
                        tempNodeInf.first = dist; tempNodeInf.second = curnode->left;
                        if(curnode->left->left == NULL && curnode->left->right==NULL){
                            bestk.pop();
                            bestk.push(tempNodeInf);
                            temp = bestk.top();
                        }else{
                            candidate.push(tempNodeInf);
                        }
                    }
                }
                if(curnode->right){
                    double dist = mbr(curnode->right, q);
                    if(dist<temp.first || (dist == temp.first && leq(curnode->right->point, temp.second->point))){
                        tempNodeInf.first = dist; tempNodeInf.second=curnode->right;
                        if(curnode->right->left == NULL && curnode->right->right==NULL){
                            bestk.pop();
                            bestk.push(tempNodeInf);
                        }else{
                            candidate.push(tempNodeInf);
                        }
                    }
                }
            }
        }
    }
    
    // optimization this with tie breaking and ascending sort
    vector<Point> answer;
    while(!bestk.empty()){
        answer.push_back(bestk.top().second->point);
        // KDTree::printPoint(bestk.top().second->point);
        bestk.pop();
    }
    std::reverse(answer.begin(),answer.end());
    return answer;
}


int main(int argc, char* argv[]) {

    char* dataset_file = argv[1];
    KDTree kdt;
    bulkInsert(dataset_file, kdt);

    // Request name/path of query_file from parent by just sending "0" on stdout
    cout << 0 << endl;

    // Wait till the parent responds with name/path of query_file and k | Timer will start now
    char* query_file = new char[100];
    int k;
    cin >> query_file >> k;
    // cerr << dataset_file << " " << query_file << " " << k << endl;
    // Point query = readQuery(query_file);
    vector<Point> query = readFile(query_file).second;
    // [TODO] Read the query point from query_file, do kNN using the kdTree and output the answer to results.txt
    const char* resultfile = "results.txt";
    std::ofstream resultFile(resultfile);
    for(int i=0;i<query.size();i++){
        vector<Point> results = knn(kdt, query[i], k);
        for(int i = 0 ; i<results.size() ; i++){
            for(int j=0 ; j<kdt.dim ; j++){
                resultFile << results[i][j] << ' ';
            }
            resultFile << "\n";
        }
    }
    resultFile.close();
    // Convey to parent that results.txt is ready by sending "1" on stdout | Timer will stop now and this process will be killed
    cout << 1 << endl;
}
