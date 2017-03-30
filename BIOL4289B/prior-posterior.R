x <- seq(0, 1, length.out=1000)

plot(x, sapply(x, function(y) dbeta(y, 10, 10)), type='l', xlab='Probability of heads', cex.lab=1.2)

par(mar=c(5,5,2,2))
plot(x, sapply(x, function(y) dbeta(y, 10, 10)), type='l', 
                xlab='Probability of heads', cex.lab=1.2, ylab='Prior/posterior', ylim=c(0,10))
lines(x, sapply(x, function(y) 5*choose(10,4) * y^4 * (1-y)^6 * dbeta(y,10,10)), col='red')
lines(x, sapply(x, function(y) 30*choose(100,40) * y^40 * (1-y)^60 * dbeta(y,10,10)), col='orange2')
lines(x, sapply(x, function(y) 200*choose(1000,400) * y^400 * (1-y)^600 * dbeta(y,10,10)), 
      col='forestgreen')
