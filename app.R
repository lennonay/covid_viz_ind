library(shiny)
library(shinythemes)
library(leaflet)
library(jsonlite)
library(showtext)
library(readr)
library(lubridate)
library(dplyr)
library(ggplot2)

#Reading covid data and setting it as a global variable to access it inside all functions
data <- readr::read_csv("data/raw/owid-covid-data.csv")
data$date <- ymd(data$date)

#Reading GeoJSON data to get country boundaries
geojson <-
  readLines(
    "https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson",
    warn = FALSE
  ) |>
  paste(collapse = "\n") |>
  jsonlite::fromJSON(simplifyVector = FALSE)

# Finding values to populate the data input widgets
countries <- c("Worldwide")
for (feature_num in seq(length(geojson[[2]]))) {
  countries <- append(countries, geojson[[2]][[feature_num]]$properties$ADMIN)
}

ui <- shinyUI(fluidPage(
  theme = my_theme,
  titlePanel("Covid-19 Tracker Dashboard"),))

server <- function(input, output) {
  thematic::thematic_shiny()}

shinyApp(ui = ui, server = server)