#include <algorithm>
#include <cctype>
#include <vector>

using namespace std;

// De memória
template <typename T> void bubblesort(vector<T> &a, int size) {
  int fim = size - 1;
  bool pronto = 0;
  T aux;
  for (int i = 0; i < size - 1; i++) {
    pronto = 1;
    for (int j = 0; j < fim; j++) {
      if (a[j] > a[j + 1]) {
        aux = a[j];
        a[j] = a[j + 1];
        a[j + 1] = aux;
        pronto = 0;
      }
    }
    if (pronto) {
      break;
    }
    fim--;
  }
}

// De memória
template <typename T> void selectionsort(vector<T> &a, int size) {
  T menorV = a[0];
  int menorI = 0;
  for (int i = 0; i < size - 1; i++) {
    menorV = a[i];
    menorI = i;
    for (int j = i; j < size; j++) {
      if (a[j] < menorV) {
        menorV = a[j];
        menorI = j;
      }
    }
    T aux = a[i];
    a[i] = a[menorI];
    a[menorI] = aux;
  }
}

///////////////////
// Insertionsort //
///////////////////

// Geeks for geeks
template <typename T> void insertionsort(vector<T> &a, int size) {
  for (int i = 1; i < size; ++i) {
    T key = a[i];
    int j = i - 1;
    while (j >= 0 && a[j] > key) {
      a[j + 1] = a[j];
      j = j - 1;
    }
    a[j + 1] = key;
  }
}

///////////////
// Shellsort //
///////////////

// Programiz
template <typename T> void shellsort(vector<T> &a, int size) {
  for (int interval = size / 2; interval > 0; interval /= 2) {
    for (int i = interval; i < size; i += 1) {
      T temp = a[i];
      int j;
      for (j = i; j >= interval && a[j - interval] > temp; j -= interval) {
        a[j] = a[j - interval];
      }
      a[j] = temp;
    }
  }
}

///////////////
// Mergesort //
///////////////

// Geeks for geeks
template <typename T> void merge(vector<T> &a, int left, int mid, int right) {

  int n1 = mid - left + 1;
  int n2 = right - mid;

  vector<T> L(n1), R(n2);

  for (int i = 0; i < n1; i++)
    L[i] = a[left + i];
  for (int j = 0; j < n2; j++)
    R[j] = a[mid + 1 + j];

  int i = 0, j = 0;
  int k = left;

  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      a[k] = L[i];
      i++;
    } else {
      a[k] = R[j];
      j++;
    }
    k++;
  }

  while (i < n1) {
    a[k] = L[i];
    i++;
    k++;
  }

  while (j < n2) {
    a[k] = R[j];
    j++;
    k++;
  }
}

template <typename T> void mergeSort(vector<T> &a, int left, int right) {
  if (left >= right)
    return;

  int mid = left + (right - left) / 2;
  mergeSort<T>(a, left, mid);
  mergeSort<T>(a, mid + 1, right);
  merge(a, left, mid, right);
}

template <typename T> void mergesort_start(vector<T> &a, int size) {
  mergeSort<T>(a, 0, size - 1);
}

////////////////
// Quicksort ///
////////////////

// Geeks for geeks

template <typename T> int partition(vector<T> &vec, int low, int high) {
  T pivot = vec[high];
  int i = (low - 1);
  for (int j = low; j <= high - 1; j++) {
    if (vec[j] <= pivot) {
      i++;
      swap(vec[i], vec[j]);
    }
  }
  swap(vec[i + 1], vec[high]);
  return (i + 1);
}

template <typename T> void quickSort(vector<T> &vec, int low, int high) {
  if (low < high) {
    int pi = partition<T>(vec, low, high);
    quickSort<T>(vec, low, pi - 1);
    quickSort<T>(vec, pi + 1, high);
  }
}

template <typename T> void quicksort_start(vector<T> &a, int size) {
  quickSort<T>(a, 0, size - 1);
}

// Heapsort //
// Geeks for geeks
template <typename T> void heapify(vector<T> &a, int n, int i) {
  int largest = i;
  int l = 2 * i + 1;
  int r = 2 * i + 2;
  if (l < n && a[l] > a[largest])
    largest = l;
  if (r < n && a[r] > a[largest])
    largest = r;
  if (largest != i) {
    swap(a[i], a[largest]);
    heapify<T>(a, n, largest);
  }
}

template <typename T> void heapsort(vector<T> &a, int n) {
  for (int i = n / 2 - 1; i >= 0; i--)
    heapify<T>(a, n, i);
  for (int i = n - 1; i >= 0; i--) {
    swap(a[0], a[i]);
    heapify<T>(a, i, 0);
  }
}
