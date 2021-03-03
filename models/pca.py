import numpy as np
from data_processing import *
from sklearn import decomposition


def select_component(pca_data, percent):
    """
    Returns the number of components such that percent% of the information is explained.

    Params
    ------
        pca_data : pca data
        percent : percentage of data explained

    Returns
    -------
        index : number of components required to meet the percentage

    """
    index = 0
    var = np.cumsum(np.round(pca_data.explained_variance_ratio_, decimals=3) * 100)
    while var[index] < percent:
        index += 1
    return index


def create_principal_components_array(dict_of_tickers, history_period='3mo'):
    """

    Parameters
    ----------
    dict_of_tickers : dict
        Dictionary containing key = Stock, value=ticker.
    history_period : str
        Corresponds to the period required to recover the prices.
        valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        Default: '3mo'

    Returns
    -------
    principal_component_array : np.array
        Array containing the main components for the selected period

    """

    # DataFrame containing CAC40 stock returns, with NaN suppression per line
    CAC40_Stocks_returns = create_stocks_df(dict_of_tickers, history_period)

    # Removal of values from the CAC40 index
    cac40_stocks_returns = CAC40_Stocks_returns.drop(['CAC40'], axis=1)

    pca = decomposition.PCA(n_components=31).fit(cac40_stocks_returns)

    # Select_component, function that calculates the number of components such that x% of the information is explained
    nb_component = select_component(pca, 95)

    array_of_principal_components = decomposition.PCA(n_components=5).fit(cac40_stocks_returns)
    array_of_principal_components = array_of_principal_components.transform(cac40_stocks_returns)

    return array_of_principal_components


if __name__ == '__main__':
    tickers_CAC40_dict = {'Air Liquide': 'AI.PA', 'Airbus': 'AIR.PA', 'Alstom': 'ALO.PA', 'ArcelorMittal': 'MT.AS',
                          'Atos': 'ATO.PA', 'AXA': 'CS.PA', 'BNP Paribas': 'BNP.PA', 'Bouygues': 'EN.PA',
                          'Capgemini': 'CAP.PA', 'Carrefour': 'CA.PA', 'Crédit Agricole': 'ACA.PA', 'Danone': 'BN.PA',
                          'Dassault Systèmes': 'DSY.PA', 'Engie': 'ENGI.PA', 'EssilorLuxottica': 'EL.PA',
                          'Hermès': 'RMS.PA', 'Kering': 'KER.PA', "L'Oréal": 'OR.PA', 'Legrand': 'LR.PA',
                          'LVMH': 'MC.PA',
                          'Michelin': 'ML.PA', 'Orange': 'ORA.PA', 'Pernod Ricard': 'RI.PA', 'Publicis': 'PUB.PA',
                          'Renault': 'RNO.PA', 'Safran': 'SAF.PA', 'Saint-Gobain': 'SGO.PA', 'Sanofi': 'SAN.PA',
                          'Schneider Electric': 'SU.PA', 'Société Générale': 'GLE.PA', 'Stellantis': 'STLA.PA',
                          'STMicroelectronics': 'STM.PA', 'Teleperformance': 'TEP.PA', 'Thales': 'HO.PA',
                          'Total': 'FP.PA', 'Unibail-Rodamco-Westfield': 'URW.AS', 'Veolia': 'VIE.PA', 'Vinci': 'DG.PA',
                          'Vivendi': 'VIV.PA', 'Worldline': 'WLN.PA'}

    period = '3mo'  # Period of history (valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max)
    # np.array containing the principal components :
    array_of_principal_component = create_principal_components_array(tickers_CAC40_dict, period)