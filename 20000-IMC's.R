n <- 20000
p <- 200000

set.seed(1234)
altura <- abs(round(rnorm(n, 1.50, 0.1), 2))

set.seed(1234)
peso <- abs(round(rnorm(n, 55, 4), 2))

IMC = c();

for (i in 1:n) {
  
  resul <- peso[i] / altura[i] ** 2
  IMC <- append(IMC, resul)
  
}

print(round(IMC, 2))