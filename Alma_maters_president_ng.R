library("tidyverse")
library("ggplot2")

# Load data
uni_data <- read_csv("president_alma_maters.csv") 

# Cleaning
uni_data <- uni_data |>
  mutate(education = if_else(startsWith(education,"Harvard"),"Harvard",education)) |>
  mutate(education = if_else(startsWith(education,"Yale"),"Yale",education)) |>
  mutate(education = if_else(startsWith(education,"Harvard"),"Harvard",education)) |>
  mutate(education = if_else(startsWith(education,"Edmund"),"Walsh School of Foreign Service",education)) |>
  mutate(education = if_else(startsWith(education,"University of North Carolina"),"University of North Carolina",education)) |>
  mutate(education = if_else(startsWith(education,"University of Cincinnati"),"University of Cincinnati",education)) |>
  mutate(education = if_else(startsWith(education,"University of Virginia"),"University of Virginia",education)) |>
  mutate(education = if_else(startsWith(education,"Columbia University"),"Columbia",education)) |>
  mutate(education = if_else(startsWith(education,"Albany Law"),"University at Albany",education)) |>
  mutate(education = if_else(startsWith(education,"Northampton"),"University of Northampton",education)) |>
  mutate(education = if_else(startsWith(education,"X"),"No Tertiary Education",education)) |>
  mutate(party_label = if_else(startsWith(party_label,"Democratic-Republican"),"Other",party_label)) |>
  mutate(party_label = if_else(startsWith(party_label,"Independent"),"Other",party_label)) |>
  mutate(party_label = if_else(startsWith(party_label,"Federalist"),"Other",party_label)) |>
  mutate(party_label = if_else(startsWith(party_label,"Whig"),"Other",party_label)) |>
  mutate(party_label = if_else(startsWith(party_label,"Know"),"Other",party_label)) |>
  mutate(party_label = if_else(startsWith(party_label,"None"),"Other",party_label))



# Bar graph
barred_data <- uni_data  |>
  count(education)

barred_data |>
  ggplot(aes(x = education, y = n)) +
  coord_flip() +
  geom_col() +
  theme_light()+
  xlab("Institution") +
  ylab("#of Presidents") +
  ggtitle("Institutions attended by U.S. President")
