library("tidyverse")
library("ggplot2")

# Load data
uni_data <- read_csv("presidential_birth_date.csv")

# Cleaning
uni_data <- uni_data |>
  mutate(education = if_else(startsWith(education,"Yale"),"Yale University",education)) |>
  mutate(education = if_else(startsWith(education,"Harvard"),"Harvard University",education)) |>
  mutate(education = if_else(startsWith(education,"Edmund"),"Walsh School of Foreign Service",education)) |>
  mutate(education = if_else(startsWith(education,"University of North Carolina"),"University of North Carolina",education)) |>
  mutate(education = if_else(startsWith(education,"University of Cincinnati"),"University of Cincinnati",education)) |>
  mutate(education = if_else(startsWith(education,"University of Virginia"),"University of Virginia",education)) |>
  mutate(education = if_else(startsWith(education,"Columbia University"),"Columbia",education)) |>
  mutate(education = if_else(startsWith(education,"Albany Law"),"University at Albany",education)) |>
  mutate(education = if_else(startsWith(education,"X"),"No Tertiary Education",education)) |>
  mutate(education = if_else(startsWith(education,"Northampton"),"University of Northampton",education)) |>
  mutate(education = ifelse(education %in% c("Harvard University", "Yale University", "Princeton Univeristy", "University of Pennsylvania"),"Ivy League", education)) |>
  mutate(education = ifelse(education %in% c("Ivy League", "No Tertiary Education"), education, "Not Ivy League"))


uni_data |>
  ggplot(aes(x = education, y = birth_date)) +
  geom_violin() +
  geom_point() +
  coord_flip() +
  theme_light() +
  xlab("Tertiary education") +
  ylab("Year") +
  ggtitle("Institutions Attended by U.S. Presidents")

