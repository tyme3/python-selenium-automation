# Created by Dimitri at 5/10/2024
Feature: Search tests

  Scenario Outline:: User can search for a product
    Given Open Target main page
    When Search for <item>
    Then Verify search results are shown for <expected_item>

Examples:
    |item         |expected_item  |
    |mug          |mug            |
    |tea          |tea            |
    |white mug    |white mug      |