data <- read.csv("../../data/train.csv")


table(data$health)/NROW(data)

test <- read.csv("../../data/test.csv")
test$uniqueid
ret <- cbind(test$uniqueid, )

m <- cbind(test$uniqueid, matrix(rep(t, 7442), nrow=7442))
colnames(m) <- c("uniqueid", "p1", "p2", "p3", "p4", "p5")

m <- as.data.frame(m)
write.csv(m, "lmao.csv", row.names = F)
