cidades <- c()
count <- 1

for (i in 1:length(city_temperature$City)) {
  
  if(length(cidades) == 0){
    cidades <- append(cidades,city_temperature$City[i])
  }
  
  if(city_temperature$City[i] != cidades[count]){
    cidades <- append(cidades,city_temperature$City[i])
    count=count+1
  }
}

temp_cidades <- data.frame(cidades)
media <- c()

for (i in 1:length(cidades)) {
  
  temp <- c()
  
  for (x in 1:length(city_temperature$AvgTemperature)) {
    if(cidades[i] == city_temperature$City[x]){
      
      temp <- append(temp, city_temperature$AvgTemperature[x])
    }
  }
  
  media <- append(media, round(mean(temp),2))
  
}

temp_cidades$media <- media

maiores <- c(0, 0, 0, 0, 0)
maior <- 1
vali <- 0
cidade = c("","","","","")

for (x in 1:5) {
  
  for (i in 1:length(temp_cidades$media)) {
    
    if(x==1){
      if(maiores[x] < temp_cidades$media[i]){
        maiores[x] = temp_cidades$media[i]
        vali = temp_cidades$media[i]
        cidade[x] = temp_cidades$cidades[i]
      }
    }
    
    if(maiores[x] < temp_cidades$media[i] & temp_cidades$media[i] < maior){
      maiores[x] = temp_cidades$media[i]
      vali = temp_cidades$media[i]
      cidade[x] = temp_cidades$cidades[i]
    }
  }
  maior = vali
  
}

final <- data.frame(cidade)
final$temperatura <- maiores

barplot(final$temperatura, col = "green", 
        main = "5 Cidades mais quentes", xlab = "Cidades", 
        ylab = "Temperatura", ylim = c(0,100), 
        names.arg = final$cidade)
grid(nx = NA, ny = NULL, col = "black")