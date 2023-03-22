# COVID Visualization Dashboard

The proposal of the dashboard can be found [here](https://github.com/lennonay/covid_viz_ind/blob/main/reports/proposal.md)

## Author

- Lennon Au-Yeung

## Usage

The dashboard can be found [here](https://covid-viz-ind.onrender.com/)

## Description of the data
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
