data = read.csv("../mysql.csv", sep = ",")

groups_statistic <- aggregate(data$time_run, by = list(type = data$account), sum)
colnames(groups_statistic) <- c("group", "run_time")

groups_median <- aggregate(data$time_wait, by = list(type = data$account), median)
colnames(groups_median) <- c("group", "median")
groups_statistic$median <- groups_median$median

groups_job <- aggregate(data$time_run, by = list(type = data$account), length)
colnames(groups_job) <- c("group", "job_counts")
groups_statistic$job_counts <- groups_job$job_counts

l = length(groups_statistic$job_counts)
# 取任务数的数量级到len
a <- c('')
for (i in 0:l){
	a[i] = nchar(groups_statistic$job_counts[i])
}
groups_statistic$len <- a

# 取任务数的数量级的平方到len2
a2 <- c('')
for (i in 0:l){
        a2[i] = nchar(groups_statistic$job_counts[i])^2
}
groups_statistic$len2 <- a2

# 取任务数的数量级的立方到len3
a3 <- c('')
for (i in 0:l){
        a3[i] = nchar(groups_statistic$job_counts[i])^3
}
groups_statistic$len3 <- a3

# 取任务数的对数到log
b <- c('')
for (i in 0:l){
        b[i] = log(groups_statistic$job_counts[i])
}
groups_statistic$log <- b

# 取任务数的开方到sqrt
c <- c('')
for (i in 0:l){
        c[i] = sqrt(groups_statistic$job_counts[i])
}
groups_statistic$sqrt <- c

# 取任务数的立方根到sqrt3
d <- c('')
for (i in 0:l){
        d[i] = groups_statistic$job_counts[i]^(1/3)
}
groups_statistic$sqrt3 <- d

write.table(groups_statistic, "groups_statistic.csv", row.names = FALSE, col.names = TRUE, sep=",", quote = FALSE)
