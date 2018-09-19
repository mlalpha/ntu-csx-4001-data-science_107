### hw_1_question


########################################################### Task 1

# 查看內建資料集: 鳶尾花(iris)資料集
iris

# 使用dim(), 回傳iris的列數與欄數
dim(iris)

# 使用head() 回傳iris的前六列
head(iris, 6)

# 使用tail() 回傳iris的後六列
tail(iris, 6)

# 使用str() 
str(iris)

# 使用summary() 查看iris敘述性統計、類別型資料概述。
summary(iris)

########################################################### Task 2

# 使用for loop 印出九九乘法表
# Ex: (1x1=1 1x2=2...1x9=9 ~ 9x1=9 9x2=18... 9x9=81)
for(i in 1:9){
    for(j in 1:9){
        cat(sprintf("%ix%i=%i\n", i, j, i*j))
        # sprintf(i)
    }
}


########################################################### Task 3

# 使用sample(), 產出10個介於10~100的整數，並存在變數 nums
nums <- sample.int(10:100, 10)

# 查看nums
nums

# 1.使用for loop 以及 if-else，印出大於50的偶數，並提示("偶數且大於50": 數字value)
# 2.特別規則：若數字為66，則提示("太66666666666了")並中止迴圈。

for(i in 0:100){
    if (i==60) {
       cat(sprintf("太66666666666了"))
       break
    }
    if(i>50 & i%%2==0){
        cat(sprintf("偶數且大於50: %i\n", i))
    }
}

    



########################################################### Task 4

# 請寫一段程式碼，能判斷輸入之西元年分 year 是否為閏年

year <- readline(prompt="Enter the year: ")
year <- strtoi(year)

while(check.integer(year)!=TRUE){
    year <- readline(prompt="Enter the year: ")
    year <- strtoi(year)
}

if((year%%4==0 & year%%100!=0) | (year%%400==0)){
    cat(sprintf("是閏年\n"))
}else{
    cat(sprintf("不是閏年\n"))
}


