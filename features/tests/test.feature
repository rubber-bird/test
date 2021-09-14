Feature: Checking functionality of ROI Calculator
  Scenario: Open
    Given Open Maestro QA Test Page
    Then Click on cookies banner
    And Click Goto calculator
    And Check if title exists Calculate your ROI on MaestroQA
    And Fillout the number of graders field with 10
    And Fillout the number of agents field with 2
    And Fillout the number of percentage field with 20
    And Click next
    Then Check if title exists Tell us a little bit more about your QA program
    And Select Spending per week
    And Click next
    Then Check if title exists Tell us more about the CX metrics you measure
    And Fillout the number of minutes of AHT with 10
    And Select First Call Resolution Rate
    And Select Number of tickets per year 10
    And Click next
    Then Check if title exists Almost Done!
    And Fillout the first name field with Mark
    And Fillout the last name field with Turchyn
    And Fillout the email field with test@go.go
    And Select the number of agents
    And Click next
    Then Check if title exists Your ROI for MaestroQA
    And Click next
    Then Check if title exists Your ROI Breakdown
