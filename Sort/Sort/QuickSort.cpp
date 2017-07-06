#include <iostream>
#include <cstdlib>
#include <time.h>

using namespace std;

class QuickSort
{
public:
  int *data;
  int length;
  QuickSort(int len);
  ~QuickSort();
  int run(int start, int end);
  void findNRankNum(int rank, int start, int end, int *NumPos);

private:
  int Parition(int start, int end);
  void Swap(int src, int dest);
};

QuickSort::QuickSort(int len)
{
  data = new int[len];
  if(data == nullptr)
  {
    cout << "Error: No Enough Space." << endl;
  }
}

QuickSort::~QuickSort()
{
  if(data != nullptr)
  {
    delete[] data;
  }
}

/*
  @func: quick sorting
  @return: error code
*/
int QuickSort::run(int start, int end)
{
  if (start>=end)
  {
    return 0;
  }
  int index = Parition(start, end);
  if(index > start){
    run(start, index - 1);
  }
  if(index+1 < end){
    run(index+1, end);
  }

  return 1;
}

int QuickSort::Parition(int start, int end)
{
  int index = start + rand()%(end - start + 1);
  int pos = start;
  int i = 0;
  Swap(index, end);

  for(i=start; i<end; i++)
  {
    if (data[i] <= data[end])
    {
      if (i!=pos)
      {
        Swap(i, pos);
      }
      pos++;
    }
  }
  Swap(end, pos);

  return pos;
}

void QuickSort::Swap(int src, int dest)
{
  int tmp = data[src];
  data[src] = data[dest];
  data[dest] = tmp;
}

/*
  @func: find the Nth large number from an int array
  @return: none
*/
void QuickSort::findNRankNum(int rank, int start, int end, int *NumPos)
{
  int bias = Parition(start, end);
  *NumPos += bias;
  if(bias < rank)
  {
    findNRankNum(rank, bias, end, NumPos);
  }
  else if(bias > rank)
  {
    *NumPos = 0;
    findNRankNum(rank, start, bias, NumPos);
  }
}


int main()
{
  int len = 20;
  QuickSort *qs = new QuickSort(len); 
  for(int i=0; i<len; i++)
  {
    qs->data[i] = rand()%100;  
  }
  clock_t ts, te;
  ts = clock();
  //qs->run(0, len-1);
  int NRankNum = 0;
  qs->findNRankNum(10, 0, len-1, &NRankNum);
  cout << "Rank 10 Num: " << qs->data[NRankNum-1] << endl;
  qs->run(0, len-1);
  te = clock();
  for(int i=0; i<len; i++)
  {
    cout << "[" << i+1 << "] " << qs->data[i] << endl;
  }
  cout << "time consume: " << te-ts << " s" << endl;  
  system("pause");
  qs->~QuickSort();
  return 1;
}