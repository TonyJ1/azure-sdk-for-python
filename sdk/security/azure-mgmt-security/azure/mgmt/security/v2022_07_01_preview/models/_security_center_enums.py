# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ApplicationConditionOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The application Condition's Operator, for example Contains for id or In for list of possible
    IDs, see examples.
    """

    CONTAINS = "Contains"
    """Checks that the string value of the data defined in Property contains the given value"""
    EQUALS = "Equals"
    """Checks that the string value of the data defined in Property equals the given value"""
    IN = "In"
    """Checks that the string value of the data defined in Property equals any of the given values
    #: (exact fit)"""


class ApplicationSourceResourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The application source, what it affects, e.g. Assessments."""

    ASSESSMENTS = "Assessments"
    """The source of the application is assessments"""
