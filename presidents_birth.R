library("tidyverse")
library("ggplot2")

# Load data
uni_data <- read_csv("presidential_birth_date.csv")

# Cleaning
uni_data <- uni_data |>
  mutate(education = if_else(startsWith(education,"None"),"No Tertiary Education", "Education"))


uni_data |>
  ggplot(aes(x = education, y = birth_date)) +
  geom_violin() +
  geom_point() + 
  theme_light() +
  xlab("") +
  ylab("") +
  ggtitle("Institutions attended by U.S. President")

