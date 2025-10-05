#include <string>
#include <iostream>
#include <fstream>
#include <utility>

#include "./algos.cpp"
#include "./algotime.hpp"

using namespace std;

void limpa_palavra(string &s) {
  s.erase(remove_if(s.begin(), s.end(),
                    [](unsigned char c) { return !isalpha(c); }),
          s.end());

  transform(s.begin(), s.end(), s.begin(),
            [](unsigned char c) { return tolower(c); });
}

void testa_ints() {
  int n = 10000;

  vector<int> nums;
  nums.reserve(n);

  for (int i = 0; i < n; i++) {
    nums.emplace_back(rand() % 500);
  }

  int n_threads = 5;

  // Tempo médio
  // cout << average_time<int>(n_threads, bubblesort<int>, nums, n) << endl;

  vector<int> nums2 = nums;
  sort(nums2.begin(), nums2.end());

  printf("a\n");
  // Tempo simples
  cout << measure_time<int>(selectionsort<int>, nums, n) << endl;
  selectionsort(nums, n);

  for (int i = 0; i < n; i++) {
    if (nums[i] != nums2[i]) {
      cout << nums[i] << " != " << nums2[i] << endl;
    }
  }
}

double testa_arquivo(string funcName,
                     function<void(vector<string> &, int)> func, int sz) {
  string inname = "../nomes" + to_string(sz) + "k.txt";
  string outname = "../ordenado" + to_string(sz) + "k" + funcName + ".txt";
  int wc = sz * 1000;

  ifstream inputFile(inname);

  if (!inputFile.is_open()) {
    cerr << "Erro abrindo arquivo: " << inname << endl;
  }

  vector<string> palavras;
  palavras.reserve(wc);

  string linha;
  while (getline(inputFile, linha)) {
    limpa_palavra(linha);
    palavras.push_back(linha);
  }

  inputFile.close();

  // for (int i = 0; i < 10; i++) {
  //   cout << palavras[i] << " ";
  // }

  cout << endl;
  cout << funcName << endl;
  cout << wc << endl;
  double time = measure_time<string>(func, palavras, wc);
  cout << time << endl;
  // selectionsort(palavras, wc);

  ofstream outFile(outname);
  for (int i = 0; i < palavras.size(); i++) {
    outFile << palavras[i] << endl;
  }
  outFile.close();

  cout << "Pronto!\n";

  return time;
}

int main() {
  vector<pair<string, function<void(vector<string> &, int)>>> funcs = {
    { "quick", quicksort_start<string>, },
    { "merge", mergesort_start<string>, },
    { "shell", shellsort<string>, },
    { "heap", heapsort<string>, },
  };

  int n_times = 5;

  double somas[funcs.size()];
  for (int i = 0; i < funcs.size(); i++) {
    somas[i] = 0;
    for (int j = 0; j < n_times; j++) {
      somas[i] += testa_arquivo(funcs[i].first, funcs[i].second, 500);
    }
  }

  for (int i = 0; i < funcs.size(); i++) {
    cout << funcs[i].first << " " << (somas[i]/n_times) << endl;
  }



  return 0;
}
