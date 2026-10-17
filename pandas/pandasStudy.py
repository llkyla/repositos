import pandas as pd

df = pd.read_csv("data.csv")


df[df['Age'] >= 23]

df[(df['Age'] >= 23)& (df['Score'] >= 80)]

df[df['Name'].str.contains("Edward")]

df.sort_values(by='Score', ascending=False)

'''
Name에 "Edward"가 포함된 행만 골라서, Score가 높은 순서로 정렬
'''
n_df = df[df['Name'].str.contains("Edward")]
n_df.sort_values(by='Score', ascending=False)
#or
df[df['Name'].str.contains("Edward")].sort_values(by='Score', ascending=False)

'''
Index,Name,Age,Score,Department
1,Edward,23,85,AI
2,John,25,72,Data
3,Edward Kim,21,91,AI
4,Alice,24,88,Data
5,Bob,22,76,AI
6,Edward Lee,27,95,Data
7,Tom,23,81,AI

다음 조건을 모두 만족하는 행을 출력해.
- Name에 "Edward"가 포함
- Age가 23 이상
- Score가 80 이상
- Department가 AI 또는 Data인 경우
- Score 내림차순 정렬
- 최종적으로 Name, Age, Score 컬럼만 출력
'''

fil_df = df[(df['Age'] >= 23) & (df['Score'] >= 80)]
fil2_df = fil_df[(fil_df['Department'] == 'AI') | (fil_df['Department'] == 'Data')]

edScore_df = fil2_df[fil2_df['Name'].str.contains("Edward")]
edScore_df = edScore_df.sort_values(by='Score', ascending=False)

answer = edScore_df[['Name', 'Age', 'Score']]

#or
answer = df[
    (df['Name'].str.contains('Edward')) &
    (df['Age'] >= 23) &
    (df['Score'] >= 80) &
    (df['Department'].isin(['AI', 'Data'])) # isin() = 이 값이 내가 지정한 여러 값 중 하나에 포함되는가
                                            # df[~df['Department'].isin(['AI', 'Data'])] 안 포함
].sort_values('Score', ascending=False)[['Name', 'Age', 'Score']]

answer.to_csv("answer.csv", index=False)

'''
Name,Department,Age,Score
Edward,AI,23,85
John,Data,25,72
Edward Kim,AI,21,91
Alice,Data,24,88
Bob,AI,22,76
Edward Lee,Data,27,95
Tom,AI,23,81
Jane,Data,26,90

다음 작업을 수행해.
1. Department별 평균 Score를 계산한다.
2. 평균 Score가 높은 Department부터 정렬한다.
3. 결과 컬럼은 Department, Score만 출력한다.
4. 평균 Score 컬럼 이름은 Score로 유지한다.
'''
answer = (
    df.groupby("Department")["Score"]
    .mean()
    .reset_index()
    .sort_values("Score", ascending=False)
)

answer.to_csv("ans.csv", index=False)

'''
groupby()       → 부서별로 묶기
["Score"]       → Score만 선택
mean()          → 평균
reset_index()   → Department를 다시 컬럼으로
sort_values()   → 평균 Score 내림차순
'''

###

'''
Name,Department,Age,Score
Edward,AI,23,85
John,Data,25,72
Edward Kim,AI,21,91
Alice,Data,24,88
Bob,AI,22,76
Edward Lee,Data,27,95
Tom,AI,23,81
Jane,Data,26,90
Mike,AI,29,94

다음 조건으로 결과를 만들어라.
1. Department별로 묶는다.
2. 각 부서의 Score 평균과 최댓값을 구한다.
3. 평균 Score가 80 이상인 부서만 남긴다.
4. 평균 Score가 높은 순으로 정렬한다.
5. 결과 컬럼은 다음 순서로 한다: Department, Avg_Score, Max_Score
'''

answer = (
    df.groupby("Department")["Score"]
    .agg(Avg_Score="mean", Max_Score="max")
    .reset_index()
)

answer = answer[answer["Avg_Score"] >= 80]
answer = answer.sort_values("Avg_Score", ascending=False)

answer.to_csv("answer.csv", index=False)

'''
students.csv
ID,Name,Department
1,Kim,AI
2,Lee,Data
3,Park,AI
4,Choi,Data

scores.csv
ID,Score
1,85
2,92
3,78
5,95

두 파일을 ID 기준으로 합쳐서 다음 결과를 만들어라.
- 모든 students를 유지
- 점수가 없는 학생도 남겨둔다
- ID, Name, Department, Score 순서
- Score가 없는 경우 0으로 처리
'''


ans = answer[answer['Max_Score'] >= 80]

ans.to_csv('answer.csv')

student = pd.read_csv("students.csv")
score = pd.read_csv("scores.csv")

res = pd.merge(student, score, on='ID', how='left')
res['Score'] = res['Score'].fillna(0)

res = res[['ID', 'Name', 'Department', 'Score']]

'''
students.csv
ID,Name,Department
1,Kim,AI
2,Lee,Data
3,Park,AI
4,Choi,Data
5,Jung,AI

projects.csv
ID,Project,Score
1,A,85
1,B,90
2,A,75
3,A,95
3,B,80
4,A,88
5,A,70
5,B,92

요구사항
1. students와 projects를 ID 기준으로 합친다.
2. 학생별 평균 Project Score를 계산한다.
3. 학생의 Name, Department도 결과에 포함한다.
4. 평균 점수가 80 이상인 학생만 남긴다.
5. 평균 점수가 높은 순으로 정렬한다.
6. 최종 컬럼:
Name, Department, Avg_Score

7. answer.csv로 저장한다.
'''

student = pd.read_csv("students.csv")
project = pd.read_csv("projects.csv")

mer_df = pd.merge(student, project, on="ID", how="left")

ans = (
    mer_df.groupby(["Name", "Department"])["Score"]
    .mean()
    .reset_index(name="Avg_Score")
)

ans = ans[ans["Avg_Score"] >= 80]
ans = ans.sort_values("Avg_Score", ascending=False)

ans.to_csv("answer.csv", index=False)

'''
employees.csv
ID,Name,Department
1,Kim,AI
2,Lee,Data
3,Park,AI
4,Choi,Data
5,Jung,AI

performance.csv
ID,Month,Score
1,Jan,80
1,Feb,90
2,Jan,70
2,Feb,85
3,Jan,95
4,Jan,60
4,Feb,80

요구사항
1. 두 DataFrame을 ID 기준으로 합친다.
2. 모든 직원이 결과에 포함되어야 한다.
3. 직원별 평균 Score를 계산한다.
4. 점수가 한 번도 없는 직원의 평균은 0으로 처리한다.
5. 평균 Score가 80 이상인 직원만 남긴다.
6. 평균 점수 내림차순으로 정렬한다.
7. 최종 컬럼:
Name, Department, Avg_Score

8. answer.csv로 저장한다.
'''
emp = pd.read_csv("employees.csv")
per = pd.read_csv("performance.csv")

df = pd.merge(emp, per, on="ID", how="left")

ans = (
    df.groupby(["Name", "Department"])["Score"]
    .mean()
    .reset_index(name="Avg_Score")
)

ans["Avg_Score"] = ans["Avg_Score"].fillna(0)
ans = ans[ans["Avg_Score"] >= 80]
ans = ans.sort_values("Avg_Score", ascending=False)
ans = ans[["Name", "Department", "Avg_Score"]]

ans.to_csv("answer.csv", index=False)


'''
products.csv 파일이 있다.
Product,Category,Price,Stock
Laptop,Electronics,1200,5
Mouse,Electronics,25,50
Keyboard,Electronics,80,20
Desk,Furniture,300,10
Chair,Furniture,150,0
Monitor,Electronics,400,8
Bookshelf,Furniture,200,3

다음 조건을 만족하는 answer.csv를 만들어라.
1. Category가 Electronics 또는 Furniture인 상품만 남긴다.
2. Stock이 0인 상품은 제외한다.
3. 각 상품의 Inventory_Value를 Price × Stock으로 계산한다.
4. Inventory_Value가 1,000 이상인 상품만 남긴다.
5. Inventory_Value가 높은 순서대로 정렬한다.
6. 최종 컬럼은 Product, Category, Inventory_Value만 남긴다.
7. answer.csv로 저장한다.
'''
df = pd.read_csv('products.csv')

df = df[df['Category'].isin(['Electronics', 'Furniture'])]
df = df[df['Stock'] != 0]

df['Inventory_Value'] = df['Price'] * df['Stock']

df = df[df['Inventory_Value'] >= 1000]
df = df.sort_values('Inventory_Value', ascending=False)
df = df[['Product', 'Category', 'Inventory_Value']]

df.to_csv('answer.csv', index=False)

'''
students.csv
ID,Name,Department,Score
1,Kim,AI,85
2,Lee,Data,92
3,Park,AI,
4,Choi,Data,78
5,Jung,AI,92
6,Han,Data,
7,Kang,AI,75
8,Yoon,Data,92

다음 조건을 만족하는 answer.csv를 만들어라.
1. Score가 결측치인 학생을 찾는다.
2. 결측치 학생은 제외한다.
3. Department별 학생 수를 계산한다.
4. 학생 수가 2명 이상인 Department만 남긴다.
5. Score가 80 이상인 학생만 남긴다.
6. Score 내림차순으로 정렬한다.
7. 최종 컬럼은 Name, Department, Score만 남긴다.
8. answer.csv로 저장한다.
'''
df = pd.read_csv('students.csv')

df = df.dropna(subset=['Score'])

counts = df['Department'].value_counts()
valid = counts[counts >= 2].index

df = df[df['Department'].isin(valid)]
df = df[df['Score'] >= 80]
df = df.sort_values('Score', ascending=False)
df = df[['Name', 'Department', 'Score']]

df.to_csv('answer.csv', index=False)

'''
orders.csv가 있다.
Order_ID,Customer,Product,Category,Price,Quantity
1,Kim,Laptop,Electronics,1200,1
2,Lee,Mouse,Electronics,25,3
3,Kim,Keyboard,Electronics,80,2
4,Park,Desk,Furniture,300,1
5,Lee,Monitor,Electronics,400,2
6,Kim,Chair,Furniture,150,4
7,Park,Mouse,Electronics,25,5
8,Choi,Desk,Furniture,300,2
9,Lee,Keyboard,Electronics,80,1

다음 조건을 만족하는 answer.csv를 만들어라.
1. 각 주문의 Total을 Price × Quantity로 계산한다.
2. Customer별 Total 합계를 계산한다.
3. 고객별 총 구매금액이 500 이상인 고객만 남긴다.
4. 총 구매금액이 높은 순서대로 정렬한다.
5. 최종 컬럼은 Customer, Total로 한다.
6. answer.csv로 저장한다.
'''

df = pd.read_csv('orders.csv')

df['Total'] = df['Price'] * df['Quantity']

df = (
    df.groupby('Customer')['Total']
    .sum()
    .reset_index()
)

df = df[df['Total'] >= 500]
df = df.sort_values('Total', ascending=False)

df.to_csv('answer.csv', index=False)

#################################
#################################
#################################

'''
문제 1 — X, y 분리
train.csv:
Age,Height,Weight,Gender
20,175,70,M
25,168,55,F
31,180,82,M
22,172,63,F

Gender가 target이다.
요구사항
- features를 X
- target을 y
- X, y를 각각 출력
'''

train = pd.read_csv("train.csv")

X = train.drop('Gender', axis=1) # axis =0 = row // =1 = col
y = train['Gender']

print(X)
print(y)

from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

X = train.drop('Gender', axis=1)
y = train['Gender']

model = RandomForestClassifier(random_state=42) # random_state=42는 아무 숫자 상관 x
model.fit(X, y) # model에서 X를 보고 y를 예측

pred = model.predict(test) # 결과가 ['F', 'M', 'F'] 라서

pred = pd.DataFrame({'Gender': pred}) # DF로 만들어줘야함
pred.to_csv("answer.csv", index=False)





###########################
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

# 정답과 입력 분리
X = train.drop('target', axis=1)
y = train['target']

# 결측치 처리 예시
X = X.fillna(X.mean(numeric_only=True))

# 범주형 변수 변환
X = pd.get_dummies(X)
test = pd.get_dummies(test)
X, test = X.align(test, join='left', axis=1, fill_value=0)

# 학습·검증 데이터 분리
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 모델 학습
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 검증 및 평가
pred = model.predict(X_valid)
print(accuracy_score(y_valid, pred))

# 전체 학습 데이터로 재학습 후 테스트 예측
model.fit(X, y)
pred = model.predict(test)

# 제출 파일 저장
answer = pd.DataFrame({'target': pred})
answer.to_csv('data/answer.csv', index=False)














###########################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

train = pd.read_csv("train.csv")

train['Age'] = train['Age'].fillna(train['Age'].mean())

X=train.drop('Gender', axis=1)
X=X.fillna(X.mean())
y=train['Gender']
'''
if Gender, 목표의 결측치 제거:
train = train.dropna(subset=['Gender'])
'''
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

model=RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_valid)

accuracy = accuracy_score(y_valid, pred)

# 결측치 개수 확인
train.isnull().sum()

# 특정 열의 결측치를 평균으로 대체
train['Age'] = train['Age'].fillna(train['Age'].mean())

# 특정 열의 결측치를 중앙값으로 대체
train['Age'] = train['Age'].fillna(train['Age'].median())

# 특정 열이 비어 있는 행 제거
train = train.dropna(subset=['Gender'])

X = pd.get_dummies(X)
test_X = pd.get_dummies(test_X)

X, test_X = X.align(test_X, join='left', axis=1, fill_value=0)

'''
1. 데이터 읽기
2. 정답 열 y와 입력 데이터 X 분리
3. 결측치·범주형 데이터 처리
4. 학습 데이터와 검증 데이터 분리
5. 모델 생성 및 학습
6. 예측 및 평가
7. 실제 테스트 데이터 예측
8. 결과 CSV 저장
'''

'''
data/train.csv를 불러온다.
Name에 Edward가 포함된 행만 선택한다.
Index, Name, Score 열만 남긴다.
Index 기준으로 오름차순 정렬한다.
결과를 data/answer.csv에 저장한다.
저장할 때 인덱스 번호는 추가하지 않는다.
'''

import pandas as pd

df = pd.read_csv("data/train.csv")

df = df[df['Name'].str.contains("Edward", na=False)]
df = df.sort_values(by='Index', ascending=True)

answer = df[['Index', 'Name', 'Score']]
answer.to_csv("data/answer.csv", index=False)

'''
CSV 파일을 불러온다.
Salary가 4000 이상인 직원만 선택한다.
Department별 직원 수(Count)와 평균 급여(AvgSalary)를 계산한다.
평균 급여 기준 내림차순 정렬한다.
결과를 data/answer.csv에 저장한다. 인덱스는 제외한다.
'''
import pandas as pd

df = pd.read_csv("data/train.csv")

df = df[df['Salary'] >= 4000]
df = (
df.groupby("Department")["Salary"]
.agg(AvgSalary="mean", Count="count")
.reset_index()
)

df = df.sort_values("AvgSalary", ascending=False)

df.to_csv("data/answer.csv", index=False)


'''
두 CSV 파일을 불러온다.
Sales가 150 이상인 판매 기록만 선택한다.
EmployeeID별 총매출을 계산한다. 총매출 열 이름은 TotalSales.
직원 정보와 총매출을 EmployeeID 기준으로 merge한다.
TotalSales 기준 내림차순으로 정렬한다.
data/answer.csv에 저장한다. 인덱스는 제외한다.
'''
import pandas as pd

sales = pd.read_csv("data/sales.csv")
employees = pd.read_csv("data/employees.csv")

sales = sales[sales['Sales'] >= 150]

ans = (
    sales.groupby("EmployeeID")["Sales"]
    .sum()
    .reset_index(name="TotalSales")
)

ans = pd.merge(ans, employees, on="EmployeeID", how="left")
ans = ans.sort_values("TotalSales", ascending=False)

ans.to_csv("data/answer.csv", index=False)


'''
CSV 파일을 불러온다.
Stock이 10 이상인 행만 선택한다.
Category별 평균 Price와 총 Stock을 계산한다.
결과 열 이름을 AvgPrice, TotalStock으로 지정한다.
TotalStock 기준 내림차순 정렬한다.
data/answer.csv에 저장한다. 인덱스는 제외한다.
'''
import pandas as pd

df = pd.read_csv("data/train.csv")

df = df[df['Stock'] >= 10]

ans = (
df.groupby("Category")[["Price", "Stock"]]
    .agg(AvgPrice="mean", TotalStock="sum")
    .reset_index()
).sort_values("TotalStock", ascending=False)

ans.to_csv("data/answer.csv", index=False)


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

# 정답과 입력 분리
X = train.drop('target', axis=1)
y = train['target']

# 결측치 처리 예시
X = X.fillna(X.mean(numeric_only=True))

# 범주형 변수 변환
X = pd.get_dummies(X)
test = pd.get_dummies(test)
X, test = X.align(test, join='left', axis=1, fill_value=0)

# 학습·검증 데이터 분리
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 모델 학습
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 검증 및 평가
pred = model.predict(X_valid)
print(accuracy_score(y_valid, pred))

# 전체 학습 데이터로 재학습 후 테스트 예측
model.fit(X, y)
pred = model.predict(test)

# 제출 파일 저장
answer = pd.DataFrame({'target': pred})
answer.to_csv('data/answer.csv', index=False)

'''
Index,Name,Age,Score,Department
1,Edward,23,85,AI
2,John,25,72,Data
3,Edward Kim,21,91,AI
4,Alice,24,88,Data
5,Bob,22,76,AI
6,Edward Lee,27,95,Data
7,Tom,23,81,AI

다음 조건을 모두 만족하는 행을 출력해.
- Name에 "Edward"가 포함
- Age가 23 이상
- Score가 80 이상
- Department가 AI 또는 Data인 경우
- Score 내림차순 정렬
- 최종적으로 Name, Age, Score 컬럼만 출력
'''

fil_df = df[(df['Age'] >= 23) & (df['Score'] >= 80)]
fil2_df = fil_df[(fil_df['Department'] == 'AI') | (fil_df['Department'] == 'Data')]

edScore_df = fil2_df[fil2_df['Name'].str.contains("Edward")]
edScore_df = edScore_df.sort_values(by='Score', ascending=False)

answer = edScore_df[['Name', 'Age', 'Score']]

#or
answer = df[
    (df['Name'].str.contains('Edward')) &
    (df['Age'] >= 23) &
    (df['Score'] >= 80) &
    (df['Department'].isin(['AI', 'Data'])) # isin() = 이 값이 내가 지정한 여러 값 중 하나에 포함되는가
                                            # df[~df['Department'].isin(['AI', 'Data'])] 안 포함
].sort_values('Score', ascending=False)[['Name', 'Age', 'Score']]

answer.to_csv("answer.csv", index=False)

'''
'''

import pandas as pd

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

age_mean = train["Age"].mean()
train["Age"] = train["Age"].fillna(age_mean)
test["Age"] = test["Age"].fillna(age_mean)

train = pd.get_dummies(train, columns=["Gender"])
test = pd.get_dummies(test, columns=["Gender"])

train, test = train.allign(
test, join="left", axis=1, fill_value=0
)

'''
data/train.csv와 data/test.csv가 주어져 있어.
- train.csv: Age, Fare, Gender, Survived
- test.csv: Age, Fare, Gender
요구사항
1. Survived를 예측할 정답 열로 설정한다.
2. Gender를 원-핫 인코딩한다.
3. 학습 데이터로 RandomForestClassifier 모델을 학습한다.
4. 테스트 데이터의 생존 여부를 예측한다.
5. 예측 결과를 data/answer.csv에 Survived 열로 저장한다. 인덱스는 저장하지 않는다.
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

X = train.drop("Survived", axis=1)
y = train["Survived"]

X = pd.get_dummies(X, columns=["Gender"])
test = pd.get_dummies(test, columns=["Gender"])

X, test = X.align(test, join="left", axis=1, fill_value=0)

X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_valid)

model.fit(X, y)
pred = model.predict(test)

ans = pd.DataFrame({"Survived": pred})
ans.to_csv("data/answer.csv", index=False)