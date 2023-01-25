library("tidyverse")
library("ggplot2")

# Load data
uni_data <- read_csv("presidents.csv") 

# Cleaning
uni_data <- uni_data |>
  mutate(education = if_else(startsWith(education,"Harvard"),"Harvard",education))


# Bar graph
barred_data <- uni_data  |>
  count(education)

barred_data |>
ggplot(aes(x = education, y = n)) +
  geom_col() +
  theme_light()+
  xlab("Institution") +
  ylab("#of Presidents")+
  ggtitle("Instituions attended by U.S. President")
