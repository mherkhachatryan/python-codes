import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import AutoMinorLocator

plt.style.use('seaborn-deep')

filename = "some_file.txt"


# data path to load data
def txt_to_df(filename):
    """
    make param to data frame object
    :param filename: be string
    :return: df: data frame object
    """

    val_to_df = []
    with open(filename, 'r') as rf:
        lines = rf.readlines()
    lines = [x.strip() for x in lines]
    lines = list(filter(None, lines))

    for line in lines:
        val_to_df.append(line.split())
    df = pd.DataFrame(val_to_df, columns=["Name", "Flux", "FluXERR", "Index", "IndexERR"])
    convert_dict = {'Name': str,
                    'Flux': float,
                    'FluXERR': float,
                    'Index': float,
                    'IndexERR': float
                    }
    df = df.astype(convert_dict)
    return df


def move_txt(data, source, h_step=1., v_step=1.):
    """
    :param data: data frame object
    :param source: be string, source name
    :param h_step: be float, horizontal movement of text
    :param v_step: be float, vertical movement of text
    :return:
    """
    df = data.copy()
    df = df.drop(df[data.Name == source].index)
    df.apply(lambda r: ax.annotate(r['Name'], (r.Flux, r.Index)), axis=1)
    data[data.Name == source].apply(lambda r: ax.annotate(r['Name'], (r.Flux * h_step, r.Index * v_step)), axis=1)


def plot_obj(filename, source, figsize=(12, 7), h_step=1., v_step=1.):
    """
    Plot and save figure
    :param filename: be string
    :param figsize: be tuple, figure size
    """
    global ax
    
    data = txt_to_df(filename)
    data.Name = data.Name.apply(lambda r: r.replace("_", " "))
    
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.errorbar(data["Flux"], data["Index"], yerr=data["IndexERR"], xerr=data["FluXERR"], lw=0, elinewidth=1.2,
                color='blue',
                fmt='o', markersize='7.5', markeredgecolor='black')

    ax.set_ylabel('Photon index', fontsize=12)
    ax.set_xlabel('F($\\gamma$) (photon $\mathregular{cm^{-2}}$ $\mathregular{s^{-1}}$)', fontsize=12)

    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.tick_params(which="minor", length=3.9)

    # move source name's text by given params
    move_txt(data, source, h_step, v_step)
    plt.savefig("plot.eps", bbox_inches='tight', format='eps', dpi=1200)
    plt.show()


plot_obj(filename, "GB1508+5714", h_step=1.04, v_step=1.01)
