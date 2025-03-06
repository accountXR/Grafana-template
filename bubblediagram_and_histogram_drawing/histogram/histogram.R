data = read.csv("../mysql.csv", sep = ",")

l = 15
duration = data$time_run
breaks = seq(0, 168, length.out = l)
duration.cut = cut(duration, breaks, right=FALSE)
duration.freq = table(duration.cut)

draw_histogram = cbind(levels(duration.cut), duration.freq)
draw_histogram = as.data.frame(draw_histogram)
colnames(draw_histogram) <- c("duration", "freq")

while(draw_histogram[8, 2] == '0')
{
	l = (l - 1) * 2 + 1
	breaks = seq(0, 168, length.out = l)
	duration.cut = cut(duration, breaks, right=FALSE)
	duration.freq = table(duration.cut)

	draw_histogram = cbind(levels(duration.cut), duration.freq)
	draw_histogram = as.data.frame(draw_histogram)
	colnames(draw_histogram) <- c("duration", "freq")
}

write.table(draw_histogram, "draw_histogram.csv", row.names = FALSE, col.names = TRUE, sep=" ", quote = FALSE)
