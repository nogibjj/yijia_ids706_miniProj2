import os
import pandas as pd
from main import load_data, calculate_statistics, create_histogram, generate_profile_report

file_path = "rdu-weather-history.csv"

def test_load_data():
    """Function to test the load_data function."""
    data = load_data(file_path)
    assert not data.empty, "Loaded data should not be empty"
    assert isinstance(data, pd.DataFrame), "Loaded data should be a DataFrame"

def test_calculate_statistics():
    """Function to test the calculate_statistics function."""
    data = load_data(file_path)
    stats = calculate_statistics(data)
    
    # Assert statements to check the calculated values against the expected values
    assert abs(stats.at["mean", "Temperature Minimum"] - 44.225166) < 1e-6, \
        "Mean of Temperature Minimum is incorrect"
    assert abs(stats.at["median", "Temperature Minimum"] - 45.000000) < 1e-6, \
        "Median of Temperature Minimum is incorrect"
    assert abs(stats.at["std_dev", "Temperature Minimum"] - 14.538763) < 1e-6, \
        "Standard deviation of Temperature Minimum is incorrect"

    assert abs(stats.at["mean", "Temperature Maximum"] - 66.966887) < 1e-6, \
        "Mean of Temperature Maximum is incorrect"
    assert abs(stats.at["median", "Temperature Maximum"] - 70.000000) < 1e-6, \
        "Median of Temperature Maximum is incorrect"
    assert abs(stats.at["std_dev", "Temperature Maximum"] - 14.719337) < 1e-6, \
        "Standard deviation of Temperature Maximum is incorrect"

    assert abs(stats.at["mean", "Precipitation"] - 0.127020) < 1e-6, \
        "Mean of Precipitation is incorrect"
    assert abs(stats.at["median", "Precipitation"] - 0.000000) < 1e-6, \
        "Median of Precipitation is incorrect"
    assert abs(stats.at["std_dev", "Precipitation"] - 0.327184) < 1e-6, \
        "Standard deviation of Precipitation is incorrect"

    # Printing the statistics for reference
    print(stats)

def test_create_histogram():
    """Function to test the create_histogram function."""
    data = load_data(file_path)
    histogram_path = "temperature_minimum_distribution.png"
    create_histogram(data, "Temperature Minimum", histogram_path)
    assert os.path.isfile(histogram_path), "Histogram file should be created"
    # os.remove(histogram_path)  # Cleanup after test

# def test_generate_profile_report():
#     """Function to test the generate_profile_report function."""
#     data = load_data(file_path)
    
#     # Define output paths
#     html_path = "profile_report.html"
#     md_path = "profile_report.md"

#     # Generate profile report
#     generate_profile_report(data, html_path, md_path)

#     # Check if the markdown file was created
#     assert os.path.isfile(md_path), "Markdown report should be created"
    
#     # Clean up by removing the created files after the test
#     # os.remove(html_path)
#     # os.remove(md_path)


if __name__ == "__main__":
    test_load_data()
    test_calculate_statistics()
    test_create_histogram()
    # test_generate_profile_report()