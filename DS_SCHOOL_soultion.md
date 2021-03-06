# numpy


## 연습 문제 4.1.6
다음 배열은 첫번째 행(row)에 학번, 두번째 행에 영어 성적, 세번째 행에 수학 성적을 적은 배열이다. 영어 성적을 기준으로 각 열(column)을 재정렬하라.

```python
array([[  1,    2,    3,    4],
       [ 46,   99,  100,   71],
       [ 81,   59,   90,  100]])
```
두번째 행(영어 성적)의 sort를 구한 후, 그 값들을 기준으로 정렬하자.

```python
a
array([[  1,   2,   3,   4],
       [ 46,  99, 100,  71],
       [ 81,  59,  90, 100]])
       
eng = np.argsort(a[1])
eng # 영어성적 기준
array([0, 3, 1, 2], dtype=int32)

a[:,eng] # 영어성적 기준 정렬
array([[  1,   4,   2,   3],
       [ 46,  71,  99, 100],
       [ 81, 100,  59,  90]])
```
