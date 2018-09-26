library(rvest)
library(XML)

htmlData <- read_html("https://movie.yahoo-leisure.hk/movie/showing?url=movie%2Fshowing")


res <- list()

title_xpath = ".title"

titles <- htmlData %>% 
  html_nodes(".each-movie") %>% 
  html_nodes(title_xpath) %>%
  html_text
  

for( title in titles){
    print(title)
}
