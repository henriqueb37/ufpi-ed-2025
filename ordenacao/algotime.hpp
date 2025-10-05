#ifndef algotime_h
#define algotime_h

#include <chrono>
#include <functional>
#include <future>
#include <vector>

using namespace std;

template <typename T>
double measure_time(function<void(vector<T> &, int)> fun, vector<T> &a,
                    int size) {
  auto start_time = chrono::high_resolution_clock::now();
  fun(a, size);
  auto end_time = chrono::high_resolution_clock::now();
  auto duration =
      chrono::duration_cast<chrono::milliseconds>(end_time - start_time);
  double tempo = duration.count();
  return tempo / 1000;
}

template <typename T>
double average_time(int n_threads, function<void(vector<T> &, int)> fun,
                    vector<T> &a, int size) {
  future<double> futuros[n_threads];
  for (int i = 0; i < n_threads; i++) {
    vector<T> cpy = a;
    futuros[i] = async(measure_time<T>, fun, cpy, size);
    // measure_time<T>(fun, cpy, size);
  }

  double soma = 0;
  for (int i = 0; i < n_threads; i++) {
    soma += futuros[i].get();
  }
  return soma / n_threads;
}

#endif
