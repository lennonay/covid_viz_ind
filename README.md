# COVID Visualization Dashboard

The proposal of the dashboard can be found [here](https://github.com/lennonay/covid_viz_ind/blob/main/reports/proposal.md)

## Author

- Lennon Au-Yeung

## Usage

The dashbaord aims to provide travellers with information regarding COVID on a worldwide level and provide them with a rough idea of the epidemic levels of their potential destinations.

The pie chart on the left displays the proportion of cases from different continents, and the map on the bottom left shows the average stringency index of countries during the COVID period.

Using the sidebar on the right, users can select a specific country they want to inquire, or select a range for the countries' median age, or a range for the countries' human development index, if they want to know if countries with similar characteristics have similar results for the COVID virus.

After selection, they are able to view new cases every month for the country and also the trend for new vaccinations. If `World` is selected and both range sldiers are at maximum, the world's new cases by month and new vaccination trend will be shown, and same for the pie chart and world map plot.

The brief questions answered by this dashboard would be:

- As a traveler one would want to know the average COVID stringency situation at the destination country.
- The impact of COVID on different countries based on median age and human development index.
- The monthly new cases of a specific country to see if COVID has slowed down

## Reference

### Description of the data

In this project, we are visualizing the COVID-19 dataset that is maintained by [_Our World in Data_](https://ourworldindata.org/coronavirus) which is present in the this [repository](https://github.com/owid/covid-19-data/tree/master/public/data). This dataset contains 59 columns corresponding to COVID-19 statistics such number of `vaccinations`, `confirmed cases`, `deaths`, `hospitalizations`, `reproduction rate`, `government policies in effect`, and other country specific information for over _219 countries_, which provides a comprehensive record of the global vaccination effort against Covid-19. These statistics are being updated constantly hence we restrict ourselves to the data collected from the start of the pandemic to **13-02-2023**. The main aim of the project is to give an overview of the ever changing COVID-19 situation in different countries to avid travelers so that they can arm themselves with the information required to plan their future travels safely.

## Get involved 

**How to run the app locally and make contributions**

If you would like to contribute to our project, please read the CONTRIBUTING.md file and then follow these steps: 
- Ensure that you have python3 installed on your computer.
- Fork the repository and [clone](https://github.com/lennonay/covid_viz_ind.git) it onto your computer.
- Create a new branch (named according to the specifications in the CONTRIBUTING.md file).

 *To run the app locally:* 

- Navigate to the source directory of the repository on the location machine.
- Ensure all the necessary packages are installed:

    `pip3 install -r requirements.txt`

- Execute the following command in a bash terminal:

    `python3 app.py`

*To propose new changes:* 
- Fork the repository
- Make your changes to the code in VSCode and adhere to best coding practices. 
- Commit your changes (with an informative commit message).
- Push your changes to your fork - Submit a pull request.

## Contributing 

Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License 

`covid_viz` was created using Dash visualization by Jenit Jain. It is licensed under the terms of the [MIT license](LICENSE).

## References

- [Our World in Data](https://ourworldindata.org/coronavirus)
- [Dataset](https://github.com/owid/covid-19-data/tree/master/public/data)
