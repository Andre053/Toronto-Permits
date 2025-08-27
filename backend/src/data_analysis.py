import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def prep_data(df):
    df["APPLICATION_DATE"] = pd.to_datetime(df["APPLICATION_DATE"])
    df["ISSUED_DATE"] = pd.to_datetime(df["ISSUED_DATE"])

    df["APPLICATION_MONTH"] = df["APPLICATION_DATE"].dt.to_period("M")

    return df



def permits_over_time(df):
    # permits can have multiple revisions, only care about the initial revision
    # filter to only permits, only first revisions, need date
    df = df[["PERMIT_NUM", "REVISION_NUM", "APPLICATION_DATE", "ISSUED_DATE"]]
    df = df[df["REVISION_NUM"] == 0]

    # add new column for month
    

    print(df.head())
    print(len(df))

    #app_date_vc = 
    value_counts = pd.Series(df.APPLICATION_MONTH).value_counts().sort_index()
    # print(app_date_vc)
    values = value_counts.index.to_timestamp()
    counts = value_counts.values

    # # TODO: review solution for plotting dates
    # #pd.plotting.register_matplotlib_converters()
    plt.plot(values, counts)
    plt.show() # shows count of revision 0 permits over time

    # plt.show()

def permits_status_types(df):
    df = df[["PERMIT_NUM", "REVISION_NUM", "APPLICATION_DATE", "ISSUED_DATE"]]
    df = df[df["REVISION_NUM"] == 0]

    

def analyze_cleared_permits(df):
    # given a raw df
    # want to analyze
    #   Permits over time
    print("Analyzing Cleared Permits")
    # get a count of all unique permits, revisions per permit
    permit_numbers = df["PERMIT_NUM"].unique()
    print("Number of permits:", len(permit_numbers))

    revision_numbers = df["REVISION_NUM"].unique()
    print("Number of revision numbers:", len(revision_numbers))

    permit_types = df["PERMIT_TYPE"].unique()
    status_types = df["STATUS"].unique()

    permits_over_time(df)



def analyze_active_permits(df):
    print("Analyzing Active Permits")

