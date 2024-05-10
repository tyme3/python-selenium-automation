# Created by Dimitri at 5/10/2024
Feature: Search tests

  Scenario: User can search for a product
    Given Open Target main page
    When Search for 'coffee'
    Then Verify search results are shown