library("tidyverse")
library("ggplot2")
library("emojifont")

load.fontawesome()
leaf <- fontawesome('fa-leaf')

# Load data
uni_data <- read_csv("president_alma_maters.csv") 

# Cleaning
uni_data <- uni_data |>
  mutate(education = if_else(startsWith(education,"Harvard"),"Harvard University",education)) |>
  mutate(education = if_else(startsWith(education,"Yale"),"Yale University",education)) |>
  mutate(education = if_else(startsWith(education,"Edmund"),"Walsh School of Foreign Service",education)) |>
  mutate(education = if_else(startsWith(education,"University of North Carolina"),"University of North Carolina",education)) |>
  mutate(education = if_else(startsWith(education,"University of Cincinnati"),"University of Cincinnati",education)) |>
  mutate(education = if_else(startsWith(education,"University of Virginia"),"University of Virginia",education)) |>
  mutate(education = if_else(startsWith(education,"Columbia"),"Columbia University",education)) |>
  mutate(education = if_else(startsWith(education,"Albany Law"),"University at Albany",education)) |>
  mutate(education = if_else(startsWith(education,"Northampton"),"University of Northampton",education)) |>
  mutate(education = if_else(startsWith(education,"X"),"No Tertiary Education",education)) |>
  mutate(party_label = if_else(startsWith(party_label,"Democratic-Republican"),"Other",party_label)) |>
  mutate(party_label = if_else(startsWith(party_label,"Independent"),"Other",party_label)) |>
  mutate(party_label = if_else(startsWith(party_label,"Federalist"),"Other",party_label)) |>
  mutate(party_label = if_else(startsWith(party_label,"Whig"),"Other",party_label)) |>
  mutate(party_label = if_else(startsWith(party_label,"Know"),"Other",party_label)) |>
  mutate(party_label = if_else(startsWith(party_label,"None"),"Other",party_label)) |>
  mutate(is_ivy = education %in% c("Harvard University", "Yale University", "Princeton Univeristy", "University of Pennsylvania", "Columbia University"))

# Bar graph
barred_data <- uni_data  |>
  group_by(party_label, education) |>
  summarise(n=n())

label_data <- uni_data |>
  filter(is_ivy) |>
  group_by(education) |>
  summarise(total_n=n())

mycolors <- c("Democrat"="#0000FF", "Other"="#808080", "Republican"="#FF0000")

barred_data |>
  group_by(education) |>
  mutate(total_n = sum(n)) |>
  ungroup() |>
  ggplot(aes(x = reorder(education, total_n), y = n)) +
  coord_flip() +
  geom_col(aes(fill = party_label)) +
  geom_text(aes(y=total_n+0.25), label=leaf, family='fontawesome-webfont', data=label_data) +
  theme_light()+
  scale_fill_manual(values=mycolors)  +
  scale_y_continuous(breaks = c(0,1,2,3,4,5,6,7,8), minor_breaks=NULL) +
  xlab("Tertiary Educational Institute") +
  ylab("Number of Presidents")
ggsave("Barplot_Presidents.pdf", width = 7, height = 5)
