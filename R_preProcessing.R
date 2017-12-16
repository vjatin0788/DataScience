#Data Processing

#importing the datasets
dataset = read.csv('Salary_Data.csv')


#install.packages('caTools')
#library('caTools')
set.seed(123)
split = sample.split(dataset$Salary,SplitRatio = 2/3)
train_set = subset(dataset,split ==TRUE)
test_set = subset(dataset,split ==FALSE)

regressor = lm(formula = Salary ~ YearsExperience,data = train_set)
summary(regressor) # if p < 5 there is strong statistical relationship & p >5 is less significant between the dependent var and independent var.
# 3 star means high statistic significance 

y_predict = predict(regressor, data = test_set)

install.packages('ggplot2')
library('ggplot2')
# plotting the train set
ggplot() +
geom_point(aes(x = train_set$YearsExperience,y = train_set$Salary),color ='red') +
geom_line(aes(x = train_set$YearsExperience,y = predict(regressor, data = train_set)),color = 'blue') +
ggtitle('Prediction') +
xlab('Years') +
ylab('Salary')
#plotting the test set
ggplot() +
  geom_point(aes(x = test_set$YearsExperience,y = test_set$Salary),color ='red') +
  geom_line(aes(x = train_set$YearsExperience,y = predict(regressor, data = train_set)),color = 'blue') +
  ggtitle('Prediction') +
  xlab('Years') +
  ylab('Salary')
