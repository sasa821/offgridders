import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def evaluate_nesp(save_subfolder):
    crf20, d20 = get_crf(20)
    pd.options.mode.chained_assignment = None

    folder = "../simulation_results/"
    path = "./Nigeria_EnergyData_Plateau.csv"
    data_set_ids = pd.read_csv(path, sep=';')
    ############ GET add Branch distances #############

    distances = pd.DataFrame([data_set_ids["Branch_id"].values, data_set_ids["Distance_m"].values / 1000,
                              data_set_ids["Distance_m"].values / 1000, data_set_ids["Distance_m"].values / 1000],
                             columns=data_set_ids.index,
                             index=['branch_id', 'original_distance_km', 'max_smaller_distance_on_branch',
                                    'add_distance_on_branch'])
    branches = {}
    theoretical_distance = 0
    for item in data_set_ids.index:
        distances[item]['max_smaller_distance_on_branch'] = 0
        theoretical_distance += data_set_ids["Distance_m"][item] / 1000
        # create branch number and change distance, if larger than existing
        if data_set_ids["Branch_id"][item] not in branches:
            branches.update({data_set_ids["Branch_id"][item]: data_set_ids["Distance_m"][item] / 1000})
        else:
            if branches[data_set_ids["Branch_id"][item]] < data_set_ids["Distance_m"][item] / 1000:
                branches.update({data_set_ids["Branch_id"][item]: data_set_ids["Distance_m"][item] / 1000})

    cost_branches = {}
    for item in branches:
        cost_branches.update({item: (branches[item] * 20000 + 20000) / branches[item]})

    for loc1 in distances.columns:
        for loc2 in distances.columns:
            if distances[loc1]['branch_id'] == distances[loc2]['branch_id']:
                if distances[loc1]['original_distance_km'] >= distances[loc2]['original_distance_km']:
                    pass
                elif distances[loc1]['original_distance_km'] != distances[loc2]['original_distance_km'] \
                        and distances[loc1]['original_distance_km'] > distances[loc2]['max_smaller_distance_on_branch']:
                    distances[loc2]['max_smaller_distance_on_branch'] = distances[loc1]['original_distance_km']

    total = 0
    for loc in distances.columns:
        distances[loc]['add_distance_on_branch'] = distances[loc]['original_distance_km'] - distances[loc][
            'max_smaller_distance_on_branch']
        total += distances[loc]['add_distance_on_branch']

    ratio = 2887 / total

    for prefix in ['reliable_', 'unreliable_']:
        number = -1

        folder_list = ["no_mgs",
                       "stage1_mgs",
                       "stage2_mgs",
                       "stage3_mgs"
                       ]
        #new_data = []
        heads = ['LCOE', 'NPV', 'NPV per HH', 'NPV per kW', 'PV kWp per kW Demand', 'Genset kW per kW Demand', 'Storage kW per kW Demand', 'Storage kWh per kW Demand']
        #for item in heads:
        #    new_data = new_data \
        #               + [item + ' ' + case in ['offgrid_mg', 'sole_maingrid', 'offgrid_mg_cons', 'offgrid_mg_cons_prod', 'ongrid_mg_cons',
        #                   'ongrid_mg_cons_prod']]


        columns = ['Peak demand kW', 'Peak demand NESP kW', 'Peak demand diff percent',
                   'PV tool kWp', 'PV NESP kWp', 'PV diff percent',
                   'Storage tool kW', 'Storage tool kWh', 'Storage NESP kWh', 'Storage diff percent',
                   'Genset tool kW', 'Genset NESP kW', 'Genset diff percent',
                   'Cost transformers USD', 'Cost extension USD',
                   'RES percent', 'Supply reliability extension percent', 'Customers ', 'Population ',
                   'Distance to national grid km', 'Additional branch distance km',
                   'LCOE USD per kWh', 'NPV USD', 'NPV per HH USD per HH', 'NPV per kW USD per kW',
                   'LCOE extension USD per kWh', 'NPV extension USD', 'NPV per HH extension USD per HH',
                   'NPV per kW extension USD per kW']
        capacities = pd.DataFrame(columns=columns)

        column_list_per_stage_totals = ['PV tool total kWp', 'PV NESP total kWp',
                                        'Storage tool total kWh', 'Storage tool total kW',
                                        'Storage NESP total kWh',
                                        'Genset tool total kW', 'Genset NESP total kW',
                                        'NPV total USD',
                                        'LCOE', 'NPV', 'NPV per HH', 'NPV per kW', 'PV kWp per kW Demand',
                                        'Genset kW per kW Demand', 'Storage kW per kW Demand',
                                        'Storage kWh per kW Demand']

        column_list_per_stage_vars = []
        for item in columns:
            column_list_per_stage_vars = column_list_per_stage_vars + [item + postfix for postfix in
                                                                       [' average', ' min', ' max', ' std']]

        column_list_per_stage = column_list_per_stage_totals + column_list_per_stage_vars

        per_stage = pd.DataFrame(index=folder_list, columns=column_list_per_stage)

        for file in folder_list:
            data = pd.read_csv(folder + "/results_" + prefix + file + ".csv", sep=',')

            name_list = []
            for item in data.index:
                if data['project_site_name'][item] not in name_list:
                    name_list.append(data['project_site_name'][item])

            capacities_stage = pd.DataFrame(index=name_list, columns=columns)
            for item in data.index:
                nesp_id = data['project_site_name'][item]
                case = data['case'][item]
                if case == 'offgrid_mg':
                    capacities_stage['Peak demand kW'][nesp_id] = data['demand_peak_kW'][item]
                    capacities_stage['PV tool kWp'][nesp_id] = data['capacity_pv_kWp'][item]
                    capacities_stage['Storage tool kWh'][nesp_id] = data['capacity_storage_kWh'][item]
                    capacities_stage['Storage tool kW'][nesp_id] = data['power_storage_kW'][item]
                    capacities_stage['Genset tool kW'][nesp_id] = data['capacity_genset_kW'][item]
                    capacities_stage['RES percent'][nesp_id] = data['res_share'][item] * 100
                    capacities_stage['LCOE USD per kWh'][nesp_id] =\
                        data['lcoe'][item] + (20000*crf20 - 3200)/data['total_demand_annual_kWh'][item]
                    capacities_stage['NPV USD'][nesp_id] = data['npv'][item] + (20000-3200/crf20)
                    capacities_stage['NPV per kW USD per kW'][nesp_id] = capacities_stage['NPV USD'][nesp_id] / \
                                                                   data['demand_peak_kW'][item]

                if case == 'sole_maingrid':
                    capacities_stage['LCOE extension USD per kWh'][nesp_id] \
                        = data['lcoe'][item]
                    capacities_stage['Cost extension USD'][nesp_id] \
                        = data['costs_maingrid_extension'][item]
                    capacities_stage['Cost transformers USD'][nesp_id] \
                        = data['costs_pcoupling'][item]

                    capacities_stage['Supply reliability extension percent'][nesp_id] \
                        = data['supply_reliability_kWh'][item]
                    capacities_stage['NPV extension USD'][nesp_id] \
                        = data['npv'][item]
                    capacities_stage['NPV per kW extension USD per kW'][nesp_id] \
                        = capacities_stage['NPV extension USD'][nesp_id] / data['demand_peak_kW'][item]

            for item in data_set_ids.index:
                name = "nesp_" + str(data_set_ids['NESP_ID'][item])
                if name in name_list:
                    capacities_stage['Additional branch distance km'][name] = distances[item][
                                                                                    'add_distance_on_branch'] * ratio
                    capacities_stage['Distance to national grid km'][name] = data_set_ids['Distance_m'][item] / 1000
                    capacities_stage['Peak demand NESP kW'][name] = data_set_ids['Demand'][item]
                    capacities_stage['Customers '][name] = data_set_ids['Customers'][item]
                    capacities_stage['Population '][name] = data_set_ids['Population'][item]
                    capacities_stage['PV NESP kWp'][name] = data_set_ids['PV size(kW)'][item]
                    capacities_stage['Storage NESP kWh'][name] = data_set_ids['Battery capacity (kWh)'][item]
                    capacities_stage['Genset NESP kW'][name] = data_set_ids['Generator capacity (kw)'][item]
                    capacities_stage['NPV per HH USD per HH'][name] = \
                        capacities_stage['NPV USD'][name] / data_set_ids['Customers'][item]
                    capacities_stage['NPV per HH extension USD per HH'][name] = \
                        capacities_stage['NPV extension USD'][name] / data_set_ids['Customers'][item]

            capacities_stage['Peak demand diff percent'] = (capacities_stage['Peak demand kW'] - capacities_stage[
                'Peak demand NESP kW']) / \
                                                       capacities_stage['Peak demand NESP kW']

            capacities_stage['PV diff percent'] = \
                (capacities_stage['PV tool kWp'] - capacities_stage['PV NESP kWp']) / capacities_stage[
                    'PV NESP kWp'] * 100
            capacities_stage['Storage diff percent'] = \
                (capacities_stage['Storage tool kWh'] - capacities_stage['Storage NESP kWh']) / capacities_stage[
                    'Storage NESP kWh'] * 100
            capacities_stage['Genset diff percent'] = \
                (capacities_stage['Genset tool kW'] - capacities_stage['Genset NESP kW']) / capacities_stage[
                    'Genset NESP kW'] * 100

            per_stage['PV tool total kWp'][file] = capacities_stage['PV tool kWp'].sum()
            per_stage['PV NESP total kWp'][file] = capacities_stage['PV NESP kWp'].sum()

            per_stage['Storage tool total kWh'][file] = capacities_stage['Storage tool kWh'].sum()
            per_stage['Storage tool total kW'][file] = capacities_stage['Storage tool kW'].sum()
            per_stage['Storage NESP total kWh'][file] = capacities_stage['Storage NESP kWh'].sum()

            per_stage['Genset tool total kW'][file] = capacities_stage['Genset tool kW'].sum()
            per_stage['Genset NESP total kW'][file] = capacities_stage['Genset NESP kW'].sum()

            per_stage['NPV total USD'][file] = capacities_stage['NPV USD'].sum()

            for item in columns:
                per_stage = add_statistics(per_stage, capacities_stage, item, file)

            capacities_stage['Diff NPV per kW USD per kW'] = capacities_stage['NPV per kW USD per kW'].values - capacities_stage[
                'NPV per kW extension USD per kW'].values
            capacities_stage['Diff NPV per HH USD per HH'] = capacities_stage['NPV per HH USD per HH'].values - capacities_stage[
                'NPV per HH extension USD per HH'].values
            capacities_stage['Diff NPV USD'] = capacities_stage['NPV USD'].values - capacities_stage[
                'NPV extension USD'].values
            capacities_stage['Diff LCOE USD per kWh'] = capacities_stage['LCOE USD per kWh'].values - capacities_stage[
                'LCOE extension USD per kWh']

            capacities_stage['Relative diff NPV per kW USD per kW'] = \
                capacities_stage['Diff NPV per kW USD per kW'].values / capacities_stage['NPV per kW USD per kW'].values

            capacities_stage['Relative diff NPV per HH USD per HH'] = \
                capacities_stage['Diff NPV per HH USD per HH'].values / capacities_stage['NPV per HH USD per HH'].values

            capacities_stage['Relative diff NPV USD'] = \
                capacities_stage['Diff NPV USD'].values / capacities_stage['NPV USD'].values

            capacities_stage['Relative diff LCOE USD per kWh'] = \
                capacities_stage['Diff LCOE USD per kWh'].values / capacities_stage['LCOE USD per kWh'].values

            if file == "stage1_mgs":
                stage1 = capacities_stage.copy()
            elif file == "stage2_mgs":
                stage2 = capacities_stage.copy()
            elif file == "stage3_mgs":
                stage3 = capacities_stage.copy()
            elif file == "no_mgs":
                no_mgs = capacities_stage.copy()

            capacities = capacities.append(capacities_stage, sort=False)

        number = plot_matrix(folder, save_subfolder, prefix, capacities, number, 'LCOE USD per kWh')

        plots = pd.DataFrame([capacities[name].values for name in
                              ['Additional branch distance km', 'Distance to national grid km',
                               'Peak demand kW', 'LCOE extension USD per kWh']],
                             index=['Additional branch distance km', 'Distance to national grid km',
                                    'Peak demand kW', 'LCOE extension USD per kWh']).transpose()
        for column in plots.columns:
            q = plots[column].quantile(0.90)
            plots = plots[plots[column] < q]

        number = number + 1
        x = 'Additional branch distance km'
        y = 'Peak demand kW'
        fig = plots.plot.hexbin(x=x, y=y, colormap='viridis', gridsize=15)
        fig.set(title="Distribution of project sites")
        plt.savefig(folder + save_subfolder + 'graph_' + prefix + str(number) + ' '+ x +' ' + y +'.png', bbox_inches="tight")
        plt.close()

        number = number + 1
        x = 'Distance to national grid km'
        fig = plots.plot.hexbin(x=x, y=y, colormap='viridis', gridsize=15)
        fig.set(title="Distribution of project sites")
        plt.savefig(folder + save_subfolder + 'graph_' + prefix + str(number) + ' '+ x +' ' + y +'.png', bbox_inches="tight")
        plt.close()

        number = number + 1
        x = 'Additional branch distance km'
        y = 'LCOE extension USD per kWh'
        fig = plots.plot.hexbin(x=x, y=y, colormap='viridis', gridsize=15)
        fig.set(title="Influence of distance form national grid")
        plt.savefig(folder + save_subfolder + 'graph_' + prefix + str(number) + ' '+ x +' ' + y +'.png', bbox_inches="tight")
        plt.close()

        number = number + 1
        x = 'Distance to national grid km'
        fig = plots.plot.hexbin(x=x, y=y, colormap='viridis', gridsize=15)
        fig.set(title="Influence of additional branch distance")
        plt.savefig(folder + save_subfolder + 'graph_' + prefix + str(number) + ' '+ x +' ' + y +'.png', bbox_inches="tight")
        plt.close()

        number = number + 1
        x = 'Additional branch distance km'
        c = 'LCOE extension USD per kWh'
        y = 'Peak demand kW'
        fig = plots.plot.hexbin(x=x, y=y, C=c, colormap='viridis', gridsize=15)
        fig.set(title="LCOE of main grid supply")
        plt.savefig(folder + save_subfolder + 'graph_' + prefix + str(number) + ' '+ x +' ' + y+' ' + c  +'.png', bbox_inches="tight")
        plt.close()

        number = number + 1
        x = 'Distance to national grid km'
        fig = plots.plot.hexbin(x=x, y=y, C=c, colormap='viridis', gridsize=15)
        fig.set(title="LCOE of main grid supply")
        plt.savefig(folder + save_subfolder + 'graph_' + prefix + str(number) + ' '+ x +' ' + y +' ' + c +'.png', bbox_inches="tight")
        plt.close()

        capacities_file = add_statistics_matrix(capacities)
        per_stage = add_statistics_matrix(per_stage)

        per_stage.to_csv(folder + save_subfolder + "nesp_comparison_" + prefix + "stages.csv")
        capacities_file.to_csv(folder + save_subfolder + "nesp_comparison_" + prefix[:-1] + ".csv")

        comparison_list_y = ['LCOE USD per kWh',
                             'NPV per HH USD per HH',
                             'Genset diff percent',
                             'Storage diff percent',
                             'PV diff percent',
                             'RES percent',
                             'NPV per kW USD per kW',
                             # 'Relative diff NPV per kW USD per kW',
                             # 'Relative diff NPV per HH USD per HH',
                             # 'Relative diff NPV USD',
                             'Relative diff LCOE USD per kWh']
        comparison_list_x = ['Peak demand kW',
                             'Distance to national grid km',
                             'Additional branch distance km',
                             'Customers ']

        number = plot_x_y_stages(folder, save_subfolder, prefix, comparison_list_x, comparison_list_y, stage1, stage2, stage3, no_mgs, number)
    return number

def plot_comparison_intercon(folder, save_subfolder, prefix, comparison_list_x, comparison_list_y, costs, number, perspective):
    color_dict = {'LCOE USD per kWh spp': (0.5803921568627451, 0.5803921568627451, 0.5803921568627451),
                  'LCOE USD per kWh offgrid_mg': (0.00392156862745098, 0.45098039215686275, 0.6980392156862745),
                  'LCOE USD per kWh ongrid_mg_cons_prod': (0.792156862745098, 0.5686274509803921, 0.3803921568627451),
                  'LCOE USD per kWh abandonment': (0.33725490196078434, 0.7058823529411765, 0.9137254901960784),
                  'LCOE USD per kWh spd': (0.9254901960784314, 0.8823529411764706, 0.2),
                  'LCOE USD per kWh ongrid_mg_cons': (0.8, 0.47058823529411764, 0.7372549019607844),
                  'LCOE USD per kWh sole_maingrid': (0.8705882352941177, 0.5607843137254902, 0.0196078431372549),
                  'LCOE USD per kWh offgrid_mg_cons': (0.00784313725490196, 0.6196078431372549, 0.45098039215686275),
                  'LCOE USD per kWh reimbursement': (0.984313725490196, 0.6862745098039216, 0.8941176470588236),
                  'LCOE USD per kWh offgrid_mg_cons_prod': (0.8352941176470589, 0.3686274509803922, 0.0)}

    for case in color_dict.copy():
        color_dict.update({case + ' mg perspective': color_dict[case]})
        color_dict.update({case + ' global perspective': color_dict[case]})
    comparison_list = comparison_list_x + comparison_list_y

    plots = pd.DataFrame([costs[name].values for name in comparison_list], index=comparison_list).transpose()
    plots_file = plots.copy()
    plots_file['NESP ID']=[str(name) for name in costs['nesp_id'].values]
    plots_file.to_csv(folder + save_subfolder + "interconnected_lcoe_" + perspective + '_' + prefix[:-1] + ".csv")
    for x in comparison_list_x:
        plotting = 0
        number += 1
        for y in comparison_list_y:
            if plotting == 0:
                fig = plots.plot.scatter(x=x, y=y, label=y[15:], color=color_dict[y]) # s=df['c'] * 200 plot THREE VALUES
                plotting = 1
            else:
                plots.plot.scatter(x=x, y=y, ax=fig, label=y[15:], color=color_dict[y])
        fig.set(ylabel='LCOE USD per kWh', title='Cost comparison, '+ perspective)
        fig.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
        plt.savefig(folder + save_subfolder + 'graph_' + prefix + str(number) + ' '+ x +' ' + y +'.png', bbox_inches="tight")
        plt.close()
    return number

def add_sum_save(folder, save_subfolder, prefix, number_of_favoured, name, perspective):
    number_of_favoured = number_of_favoured.append(
        pd.DataFrame([number_of_favoured[column].values.sum() for column in number_of_favoured.columns],
                     columns=['sum'], index=number_of_favoured.columns).transpose(), sort=False)
    #print(folder + save_subfolder + name + "_" + perspective + '_' + prefix[:-1] + ".csv")
    number_of_favoured.to_csv(folder + save_subfolder + name + perspective + '_' + prefix[:-1] + ".csv")

def compare_solutions(costs, file, favoured, number_of_favoured, case_name, case_list, comparison_value, perspective):
    favoured[case_name] = [0 for entry in costs.index]
    for item in costs.index:
        for specific_case in case_list:
            list = case_list.copy()
            list.remove(specific_case)
            if costs[comparison_value + specific_case+perspective][item] \
                    < min([costs[comparison_value + case +perspective][item] for case in list]):
                favoured[case_name][item] = specific_case
                number_of_favoured[specific_case + perspective][file] = number_of_favoured[specific_case + perspective][file] + 1

    return favoured, number_of_favoured

def add_statistics(per_stage, capacities_stage, column_name, file):
    per_stage[column_name + ' average'][file] = capacities_stage[column_name].mean()
    per_stage[column_name + ' min'][file] = capacities_stage[column_name].min()
    per_stage[column_name + ' max'][file] = capacities_stage[column_name].max()
    per_stage[column_name + ' std'][file] = capacities_stage[column_name].std()
    return per_stage

def add_statistics_matrix(matrix):
    add = pd.DataFrame({'sum': [matrix[column].values.sum() for column in matrix.columns],
                        'average':[matrix[column].values.mean() for column in matrix.columns],
                        'max':[matrix[column].values.max() for column in matrix.columns],
                        'min':[matrix[column].values.min() for column in matrix.columns]
                        }, index=matrix.columns)
    matrix = matrix.append(add.transpose(), sort=False)
    return matrix

def plot_x_y_stages(folder, save_subfolder, prefix, comparison_list_x, comparison_list_y, stage1, stage2, stage3, no_mgs, number):

    comparison_list = comparison_list_y + comparison_list_x
    plots_1 = pd.DataFrame([stage1[name].values for name in comparison_list], index=comparison_list).transpose()
    plots_2 = pd.DataFrame([stage2[name].values for name in comparison_list], index=comparison_list).transpose()
    plots_3 = pd.DataFrame([stage3[name].values for name in comparison_list], index=comparison_list).transpose()
    plots_no = pd.DataFrame([no_mgs[name].values for name in comparison_list], index=comparison_list).transpose()

    for x_value in comparison_list_x:
        for y_value in comparison_list_y:
            if x_value != y_value:
                number += 1
                fig = plots_no.plot.scatter(x=x_value, y=y_value, color='#cc0000', label='No MGs')
                plots_2.plot.scatter(x=x_value, y=y_value, ax=fig, color='#0033cc', label='Stage 2')
                plots_3.plot.scatter(x=x_value, y=y_value, ax=fig, color='#990099', label='Stage 3')
                plots_1.plot.scatter(x=x_value, y=y_value, ax=fig, color='#66cc33', label='Stage 1')
                fig.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
                fig.set(title='Comparison of trends in stages')
                plt.savefig(folder + save_subfolder + 'graph_' + prefix + str(number) + ' '+ x_value +' ' + y_value +'.png', bbox_inches="tight")
                plt.close()

    return number

def plot_matrix(folder, save_subfolder, prefix, matrix, number, c):
    x = 'Additional branch distance km' # 'Distance to national grid km'
    y = 'Peak demand kW'
    number += 1
    plots = pd.DataFrame([matrix[name].values for name in [x,y,c]], index=[x,y,c]).transpose()
    # Delete all outliners, so that 90% of the values remain
    for column in plots.columns:
        q = plots[column].quantile(0.90)
        plots = plots[plots[column] < q]
    number += 1
    fig = plots.plot.hexbin(x=x, y=y, C=c, colormap='viridis', gridsize=30)
    fig.set(title=c)
    plt.savefig(folder + save_subfolder + 'graph_' + prefix + str(number) + ' '+ x +' ' + y +' ' + c  + '.png', bbox_inches="tight")
    plt.close()
    return number

def get_crf (grid_arrival):
    wacc = 0.16
    crf = (wacc * (1+ wacc) ** grid_arrival) / ((1+wacc) ** grid_arrival - 1)
    d = ((1+ wacc) ** grid_arrival)
    return  crf, d

def evaluate_grid_arrival_time(grid_arrival, save_subfolder):

    if grid_arrival == 5:
        number_5 = evaluate_nesp('evaluation/')

    pd.options.mode.chained_assignment = None

    folder = "../simulation_results/"

    path = "./Nigeria_EnergyData_Plateau.csv"
    data_set_ids = pd.read_csv(path, sep=';')
    crf_t, d_t = get_crf(grid_arrival)
    crf_20, d_20 = get_crf(20)
    crf_20_t, d_20_t= get_crf(20-grid_arrival)

    fit = 0.05
    pel_national = 0.08
    revenue_margin = 0.02

    folder_list = ["no_mgs",
                   "stage1_mgs",
                   "stage2_mgs",
                   "stage3_mgs"
                   ]

    ############ GET add Branch distances #############


    distances = pd.DataFrame([data_set_ids["Branch_id"].values, data_set_ids["Distance_m"].values/1000, data_set_ids["Distance_m"].values/1000, data_set_ids["Distance_m"].values/1000],
                             columns = data_set_ids.index,
                             index=['branch_id', 'original_distance_km', 'max_smaller_distance_on_branch', 'add_distance_on_branch'])
    branches = {}
    theoretical_distance = 0
    for item in data_set_ids.index:
        distances[item]['max_smaller_distance_on_branch']=0
        theoretical_distance += data_set_ids["Distance_m"][item]/1000
        # create branch number and change distance, if larger than existing
        if data_set_ids["Branch_id"][item] not in branches:
            branches.update({data_set_ids["Branch_id"][item]: data_set_ids["Distance_m"][item]/1000})
        else:
            if branches[data_set_ids["Branch_id"][item]] < data_set_ids["Distance_m"][item]/1000:
                branches.update({data_set_ids["Branch_id"][item]: data_set_ids["Distance_m"][item]/1000})

    cost_branches = {}
    for item in branches:
        cost_branches.update({item: (branches[item] * 20000 + 20000)/branches[item]})

    for loc1 in distances.columns:
        for loc2 in distances.columns:
            if distances[loc1]['branch_id']==distances[loc2]['branch_id']:
                if distances[loc1]['original_distance_km'] >= distances[loc2]['original_distance_km']:
                    pass
                elif distances[loc1]['original_distance_km'] != distances[loc2]['original_distance_km'] \
                        and distances[loc1]['original_distance_km'] > distances[loc2]['max_smaller_distance_on_branch']:
                    distances[loc2]['max_smaller_distance_on_branch'] = distances[loc1]['original_distance_km']

    total = 0
    for loc in distances.columns:
        distances[loc]['add_distance_on_branch'] = distances[loc]['original_distance_km']- distances[loc]['max_smaller_distance_on_branch']
        total += distances[loc]['add_distance_on_branch']

    ratio = 2887/total

    for prefix in ['reliable_', 'unreliable_']:
        number = -1
        title_costs = ['Autonomy percent', 'LCOE USD per kWh', 'NPV USD', 'NPV per HH USD per HH', 'NPV per kW USD per kW']
        title_costs_2 = ['LCOE USD per kWh', 'NPV USD', 'NPV per HH USD per HH', 'NPV per kW USD per kW']
        list_cases_small = ['offgrid_mg', 'sole_maingrid', 'offgrid_mg_cons', 'offgrid_mg_cons_prod', 'ongrid_mg_cons',
                            'ongrid_mg_cons_prod']
        list_cases = ['offgrid_mg', 'sole_maingrid', 'offgrid_mg_cons', 'offgrid_mg_cons_prod', 'ongrid_mg_cons',
                      'ongrid_mg_cons_prod', 'reimbursement', 'abandonment', 'spp', 'spd']

        costs_titles = ['Peak demand kW',
                        'Customers ',
                        'reliability ',
                        'Distance to national grid km',
                        'Additional branch distance km',
                        'annual demand kWh/a',
                        'Grid extension incl pcc USD',
                        'distribution grid costs USD',
                        'PV CAP',
                        'MG costs until grid arrival USD',
                        'abandonment USD',
                        'profit loss at termination USD',
                        'spd abandonement USD',
                        'spd future operation costs USD',
                        'solar generation annual kWh/a',
                        'solar generation peak [kW/kWp]',
                        'solar generation [kWh/a/kWp]',
                        'spp upgrade costs USD',
                        'spp abandonement USD',
                        'spp future operation costs USD',
                        'reimbursement distribution grid USD',
                        'reimbursement all equipment USD',
                        'Supply from grid kWh sole_maingrid'
                        ]

        for item in title_costs:
            costs_titles = costs_titles + [item + ' ' + postfix for postfix in list_cases_small]

        for item in title_costs_2:
            costs_titles = costs_titles + [item + ' ' + postfix + ' mg perspective' for postfix in list_cases] \
                           + [item + ' ' + postfix + ' global perspective' for postfix in list_cases]

        costs = pd.DataFrame(np.zeros((0, len(costs_titles))), columns=costs_titles)

        case_list_aspect1 = ['offgrid_mg', 'sole_maingrid']

        if prefix == 'unreliable_':
            case_list_aspect2_on_off = ['offgrid_mg', 'offgrid_mg_cons', 'offgrid_mg_cons_prod']
            case_list_aspect2_on = ['offgrid_mg_cons', 'offgrid_mg_cons_prod']
            case_list_aspect3_on_off = ['offgrid_mg', 'offgrid_mg_cons', 'offgrid_mg_cons_prod', 'ongrid_mg_cons',
                                        'ongrid_mg_cons_prod']
            case_list_aspect3_on = ['offgrid_mg_cons_prod', 'ongrid_mg_cons', 'ongrid_mg_cons_prod']
            case_list_aspect3_adapt = ['offgrid_mg_cons', 'offgrid_mg_cons_prod', 'offgrid_mg_cons',
                                       'ongrid_mg_cons_prod']

        else:
            case_list_aspect2_on_off = ['offgrid_mg', 'sole_maingrid', 'offgrid_mg_cons', 'offgrid_mg_cons_prod']
            case_list_aspect2_on = ['sole_maingrid', 'offgrid_mg_cons', 'offgrid_mg_cons_prod']
            case_list_aspect3_on_off = ['offgrid_mg', 'sole_maingrid', 'offgrid_mg_cons', 'offgrid_mg_cons_prod',
                                        'ongrid_mg_cons', 'ongrid_mg_cons_prod']
            case_list_aspect3_on = ['offgrid_mg_cons_prod', 'ongrid_mg_cons', 'ongrid_mg_cons_prod']
            case_list_aspect3_adapt = ['offgrid_mg_cons', 'offgrid_mg_cons_prod', 'ongrid_mg_cons',
                                       'ongrid_mg_cons_prod', 'spp', 'spd', 'reimbursement', 'abandonment',
                                       'sole_maingrid']

        case_list_aspect3_all = ['offgrid_mg_cons', 'offgrid_mg_cons_prod', 'ongrid_mg_cons', 'ongrid_mg_cons_prod',
                                 'reimbursement', 'abandonment', 'spp', 'spd']

        case_list_aspect1_perspectives = [name + ' global perspective' for name in list_cases] + [
            name + ' mg perspective' for name in case_list_aspect1]
        case_list_aspect2_on_off_perspectives =  [name for name in list_cases] + [name + ' global perspective' for name in list_cases] + [
            name + ' mg perspective' for name in case_list_aspect2_on_off]
        case_list_aspect2_on_perspectives = [name for name in list_cases] + [name + ' global perspective' for name in list_cases] + [
            name + ' mg perspective' for name in case_list_aspect2_on]
        case_list_aspect3_on_off_perspectives = [name + ' global perspective' for name in list_cases] + [
            name + ' mg perspective' for name in case_list_aspect3_on_off]
        case_list_aspect3_on_perspectives = [name + ' global perspective' for name in list_cases] + [
            name + ' mg perspective' for name in case_list_aspect3_on]
        case_list_aspect3_all_perspectives = [name + ' global perspective' for name in list_cases] + [
            name + ' mg perspective' for name in case_list_aspect3_all]
        case_list_aspect3_adapt_perspectives = [name + ' global perspective' for name in list_cases] + [
            name + ' mg perspective' for name in case_list_aspect3_adapt]

        number_of_favoured = pd.DataFrame(np.zeros((len(folder_list), len(list_cases) * 3)), index=folder_list,
                                          columns=[name for name in list_cases]  + [name + ' global perspective' for name in list_cases] + [
                                              name + ' mg perspective' for name in list_cases])
        # for i in number_of_favoured.index:
        #    for j in number_of_favoured.columns:
        #        number_of_favoured[j][i] = 0

        number_of_favoured_aspect1 = number_of_favoured[case_list_aspect1_perspectives].copy()
        number_of_favoured_aspect2_on_off = number_of_favoured[case_list_aspect2_on_off_perspectives].copy()
        number_of_favoured_aspect2_on = number_of_favoured[case_list_aspect2_on_perspectives].copy()
        number_of_favoured_aspect3_on_off = number_of_favoured[case_list_aspect3_on_off_perspectives].copy()
        number_of_favoured_aspect3_on = number_of_favoured[case_list_aspect3_on_perspectives].copy()
        number_of_favoured_aspect3_npv = number_of_favoured[case_list_aspect3_all_perspectives].copy()
        number_of_favoured_aspect3_lcoe = number_of_favoured[case_list_aspect3_all_perspectives].copy()
        number_of_favoured_aspect3_adapt_lcoe = number_of_favoured[case_list_aspect3_adapt_perspectives].copy()

        for file in folder_list:
            data = pd.read_csv(folder + "/results_" + prefix + file + ".csv", sep=',')

            name_list = []
            for item in data.index:
                if data['project_site_name'][item] not in name_list:
                    name_list.append(data['project_site_name'][item])

            costs_stage = pd.DataFrame(np.zeros((len(name_list), len(costs_titles))), index=name_list,
                                       columns=costs_titles)

            for item in data_set_ids.index:
                name = "nesp_" + str(data_set_ids['NESP_ID'][item])
                if name in name_list:
                    costs_stage['Additional branch distance km'][name] = distances[item][
                                                                               'add_distance_on_branch'] * ratio
                    costs_stage['Customers '][name] = data_set_ids['Customers'][item]
                    costs_stage['Distance to national grid km'][name] = data_set_ids['Distance_m'][item] / 1000
                    generation = pd.read_csv('../inputs/timeseries/' + name + '.csv', sep=';')
                    costs_stage['solar generation [kWh/a/kWp]'][name] = generation['SolarGen'].sum()
                    costs_stage['solar generation peak [kW/kWp]'][name] = generation['SolarGen'].max()

            for item in data.index:
                case = data['case'][item]
                if case in list_cases:
                    nesp_id = data['project_site_name'][item]

                    costs_stage['Autonomy percent ' + case][nesp_id] = data['autonomy_factor'][item]
                    costs_stage['Peak demand kW'][nesp_id] = data['demand_peak_kW'][item]
                    costs_stage['annual demand kWh/a'][nesp_id] = data['total_demand_annual_kWh'][item]
                    costs_stage['distribution grid costs USD'][nesp_id] = data['costs_distribution_grid'][item]

                    costs_stage['LCOE USD per kWh ' + case][nesp_id] = \
                        data['lcoe'][item] + (20000 * crf_20 - 3200) / data['total_demand_annual_kWh'][item]
                    costs_stage['NPV USD ' + case][nesp_id] = data['npv'][item]  + (20000 - 3200 / crf_20)

                    costs_stage['NPV per kW USD per kW ' + case][nesp_id] = \
                        costs_stage['NPV USD ' + case][nesp_id] / data['demand_peak_kW'][item]
                    costs_stage['NPV per HH USD per HH ' + case][nesp_id] = \
                        costs_stage['NPV USD ' + case][nesp_id] / costs_stage['Customers '][nesp_id]

                    if case == 'sole_maingrid':
                        costs_stage['Supply from grid kWh ' + case][nesp_id] = \
                            data['consumption_main_grid_mg_side_annual_kWh'][item]

                        costs_stage['Grid extension incl pcc USD'][nesp_id] = \
                            (data['annuity_maingrid_extension'][item] + data['annuity_pcoupling'][
                                item])/ crf_20_t / d_t

                        costs_stage['reliability '][nesp_id] = data['supply_reliability_kWh'][item]
                    if case == 'ongrid_mg_cons': #todo check
                        costs_stage['spp upgrade costs USD'][nesp_id] = \
                            (data['annuity_pcoupling'][item] / data['capacity_pcoupling_kW'][item])

                    if case == 'offgrid_mg':
                        costs_stage['PV CAP'][nesp_id] = data['capacity_pv_kWp'][item]
                        costs_stage['spp upgrade costs USD'][nesp_id] = \
                            costs_stage['spp upgrade costs USD'][nesp_id]  / crf_20_t  / d_t * \
                            costs_stage['solar generation peak [kW/kWp]'][nesp_id] * costs_stage['PV CAP'][nesp_id]

                        # sum up ALL annual costs until national grid arrival, including fuel
                        costs_stage['MG costs until grid arrival USD'][nesp_id] = data['annuity'][item] / crf_t

                        # get mg costs that occurr after grid arrives (assuming battery replacements!), ie.
                        # all npv minus the already paid annuities (including fuel costs) minus future fuel costs
                        # (add fuel costs until t to be able to substract full value
                        costs_stage['abandonment USD'][nesp_id] = (data['annuity'][item] -
                                                                     data['expenditures_fuel_annual'][item]) / crf_20_t / d_t

                        # lost profit is revenue margin of sold electricity
                        costs_stage['profit loss at termination USD'][nesp_id] = \
                            data['total_demand_annual_kWh'][item] * (data['lcoe'][item] * revenue_margin) / crf_20_t / d_t

                        # abandonement costs of spd differ, as distribution grid is further utilized!
                        costs_stage['spd abandonement USD'][nesp_id] = \
                            costs_stage['abandonment USD'][nesp_id] \
                            - (data['annuity_distribution_grid'][item]) / crf_20_t / d_t

                        costs_stage['spd future operation costs USD'][nesp_id] \
                            = (data['annuity_distribution_grid'][item]) /crf_20_t / d_t

                        # abandonement costs of spp differ, as inverters and pv are further utilized!
                        costs_stage['spp abandonement USD'][nesp_id] = \
                            costs_stage['abandonment USD'][nesp_id] \
                            - (data['annuity_pv'][item]) / crf_20_t / d_t

                        costs_stage['spp future operation costs USD'][nesp_id] \
                            = costs_stage['spp upgrade costs USD'][nesp_id] + \
                              + (data['annuity_pv'][item]+data['annuity_inverter_dc_ac'][item]) / crf_20_t / d_t

                        # present value of reimbursement of distribution cost - annuities until arrival paid, rest value
                        costs_stage['reimbursement distribution grid USD'][nesp_id] = \
                            (data['annuity_distribution_grid'][item]) / crf_20_t /d_t

                        # present value of reimbursement of all equipment cost - annuities until arrival paid
                        # AND revenues for one year (not profit margin!)
                        costs_stage['reimbursement all equipment USD'][nesp_id] = \
                            costs_stage['abandonment USD'][nesp_id]\
                            + (data['lcoe'][item] * data['total_demand_annual_kWh'][item] * (1 + revenue_margin)) / d_t

            # (2) npv of reimbursement includes investment costs up till arrival and abandonment costs which are equalled out by reimbursement
            costs_stage['NPV USD reimbursement mg perspective'] = costs_stage['MG costs until grid arrival USD'] \
                                                                    + costs_stage['abandonment USD'] \
                                                                    - costs_stage['reimbursement all equipment USD']

            costs_stage['solar generation annual kWh/a'] = costs_stage['solar generation [kWh/a/kWp]'] * costs_stage[
                'PV CAP']
            costs_stage['spp feed-in [USD per a]'] = costs_stage['solar generation annual kWh/a'] * fit
            # (3) npv of spp includes investments until now, abandonment costs, reimbursements for distribution grid and solar feed-in over the next years.
            costs_stage['NPV USD spp mg perspective'] = costs_stage['MG costs until grid arrival USD'] \
                                                          + costs_stage['spp abandonement USD'] \
                                                          - costs_stage['reimbursement distribution grid USD'] \
                                                          + costs_stage['spp future operation costs USD'] \
                                                          - costs_stage['spp feed-in [USD per a]'] / d_t / crf_20_t

            # (4) abandonment mg is operated until grid arrives, then terminated
            costs_stage['NPV USD abandonment mg perspective'] = costs_stage['MG costs until grid arrival USD'] \
                                                                  + costs_stage['abandonment USD'] \
                # + costs_stage['profit loss at termination USD']

            # (5) npv of spd includes investments until now, abandonment costs of all generation units, continued
            # operation of distribution grid and retail margin over the following years
            costs_stage['NPV USD spd mg perspective'] = costs_stage['MG costs until grid arrival USD'] \
                                                          + costs_stage['spd abandonement USD'] \
                                                          + costs_stage['spd future operation costs USD'] \
                                                          - costs_stage['annual demand kWh/a'] * costs_stage['reliability '] * (
                                                                      pel_national * revenue_margin) / d_t / crf_20_t

            for item in ['reimbursement', 'abandonment', 'spp', 'spd']:
                costs_stage['LCOE USD per kWh ' + item + ' mg perspective'] = \
                    costs_stage['NPV USD ' + item + ' mg perspective'] * crf_t \
                    / (costs_stage['annual demand kWh/a'])

                costs_stage['NPV USD ' + item + ' global perspective'] = \
                    costs_stage['NPV USD ' + item + ' mg perspective'] + costs_stage['Grid extension incl pcc USD'] \
                    + (costs_stage['annual demand kWh/a'] * costs_stage['reliability ']* pel_national) / crf_20_t /d_t

                if item == 'spp':
                    costs_stage['NPV USD ' + item + ' global perspective'] = \
                        costs_stage['NPV USD ' + item + ' global perspective'] \
                        + costs_stage['reimbursement distribution grid USD']

                elif item == 'abandonment':
                    costs_stage['NPV USD ' + item + ' global perspective'] = \
                        costs_stage['NPV USD ' + item + ' global perspective'] \
                        + costs_stage['distribution grid costs USD']/d_t

                elif item == 'reimbursement':
                    costs_stage['NPV USD ' + item + ' global perspective'] = \
                        costs_stage['NPV USD ' + item + ' global perspective'] \
                        + costs_stage['reimbursement all equipment USD']

                costs_stage['LCOE USD per kWh ' + item + ' global perspective'] = \
                    costs_stage['NPV USD ' + item + ' global perspective'] \
                        / (costs_stage['annual demand kWh/a']/crf_t + costs_stage['reliability ']*costs_stage['annual demand kWh/a'] /crf_20_t/d_t)


            for item in ['offgrid_mg', 'sole_maingrid', 'offgrid_mg_cons', 'offgrid_mg_cons_prod', 'ongrid_mg_cons',
                         'ongrid_mg_cons_prod']:
                if item == 'sole_maingrid':
                    costs_stage['NPV USD ' + item + ' mg perspective'] = \
                        (costs_stage['NPV USD ' + item] / d_t - costs_stage['Grid extension incl pcc USD'])

                    costs_stage['NPV USD ' + item + ' global perspective'] = costs_stage['NPV USD ' + item] / d_t

                    costs_stage['LCOE USD per kWh ' + item + ' mg perspective'] = \
                        costs_stage['NPV USD ' + item + ' mg perspective'] \
                        / (costs_stage['reliability ']*costs_stage['annual demand kWh/a'] /crf_20/d_t)

                    costs_stage['LCOE USD per kWh ' + item + ' global perspective'] = \
                        costs_stage['NPV USD ' + item + ' global perspective'] \
                        / (costs_stage['reliability ']*costs_stage['annual demand kWh/a'] /crf_20/d_t)

                else:
                    if item == "offgrid_mg":
                        costs_stage['NPV USD ' + item + ' mg perspective'] = \
                            costs_stage['NPV USD offgrid_mg'] #* crf_20 / crf_t + costs_stage['NPV USD ' + item] * crf_20 / crf_20_t / d_t
                    else:
                        costs_stage['NPV USD ' + item + ' mg perspective'] = \
                            costs_stage['NPV USD offgrid_mg'] * crf_20 / crf_t +\
                            costs_stage['NPV USD ' + item] * crf_20 / crf_20_t / d_t \
                            - costs_stage['Grid extension incl pcc USD']

                    costs_stage['LCOE USD per kWh ' + item + ' mg perspective'] = \
                        costs_stage['NPV USD ' + item + ' mg perspective'] * crf_20 \
                        / costs_stage['annual demand kWh/a']

                    if item == "offgrid_mg":
                        costs_stage['NPV USD ' + item + ' global perspective'] = \
                        costs_stage['NPV USD ' + item + ' mg perspective']
                    else:
                        costs_stage['NPV USD ' + item + ' global perspective'] = \
                            costs_stage['NPV USD ' + item + ' mg perspective'] \
                            + costs_stage['Grid extension incl pcc USD']

                    costs_stage['LCOE USD per kWh ' + item + ' global perspective'] = \
                        costs_stage['NPV USD ' + item + ' global perspective'] * crf_20 / \
                        costs_stage['annual demand kWh/a']

            for perspective in [' mg perspective', ' global perspective']:

                for item in list_cases:
                    costs_stage['NPV per kW USD per kW ' + item + perspective] = \
                        costs_stage['NPV USD ' + item + perspective] / \
                        costs_stage['Peak demand kW']

                    costs_stage['NPV per HH USD per HH ' + item + perspective] = \
                        costs_stage['NPV USD ' + item + perspective] / \
                        costs_stage['Customers ']

                favoured = pd.DataFrame(index=costs_stage.index)
                favoured, number_of_favoured_aspect1 \
                    = compare_solutions(costs_stage, file, favoured, number_of_favoured_aspect1, 'favoured_aspect1',
                                        case_list_aspect1, 'LCOE USD per kWh ', perspective)

                favoured, number_of_favoured_aspect2_on_off \
                    = compare_solutions(costs_stage, file, favoured, number_of_favoured_aspect2_on_off,
                                        'favoured_aspect2_on_off', case_list_aspect2_on_off, 'LCOE USD per kWh ',
                                        perspective)

                favoured, number_of_favoured_aspect2_on \
                    = compare_solutions(costs_stage, file, favoured, number_of_favoured_aspect2_on,
                                        'favoured_aspect2_on_off_npv_kW', case_list_aspect2_on,
                                        'NPV per kW USD per kW ', perspective)

                favoured, number_of_favoured_aspect3_on_off \
                    = compare_solutions(costs_stage, file, favoured, number_of_favoured_aspect3_on_off, 'favoured_aspect2_on',
                                        case_list_aspect3_on_off, 'LCOE USD per kWh ', perspective)

                favoured, number_of_favoured_aspect3_on \
                    = compare_solutions(costs_stage, file, favoured, number_of_favoured_aspect3_on, 'favoured_aspect3_on_off',
                                        case_list_aspect3_on, 'LCOE USD per kWh ', perspective)

                favoured, number_of_favoured_aspect3_npv \
                    = compare_solutions(costs_stage, file, favoured, number_of_favoured_aspect3_npv,
                                        'favoured_aspect3_all_npv_kw', case_list_aspect3_all, 'NPV per kW USD per kW ',
                                        perspective)

                favoured, number_of_favoured_aspect3_lcoe \
                    = compare_solutions(costs_stage, file, favoured, number_of_favoured_aspect3_lcoe,
                                        'favoured_aspect3_all_lcoe', case_list_aspect3_all, 'LCOE USD per kWh ',
                                        perspective)

                favoured, number_of_favoured_aspect3_adapt_lcoe \
                    = compare_solutions(costs_stage, file, favoured, number_of_favoured_aspect3_adapt_lcoe,
                                        'favoured_aspect3_adapt_lcoe', case_list_aspect3_adapt, 'LCOE USD per kWh ',
                                        perspective)
            # print(favoured)
            # print(number_of_favoured_aspect3_adapt_lcoe)

            favoured, number_of_favoured_aspect2_on_off \
                 = compare_solutions(costs_stage, file, favoured, number_of_favoured_aspect2_on_off,
                                     'favoured_aspect2_on_off', case_list_aspect2_on_off, 'LCOE USD per kWh ',
                                     '')

            favoured, number_of_favoured_aspect2_on \
                 = compare_solutions(costs_stage, file, favoured, number_of_favoured_aspect2_on,
                                     'favoured_aspect2_on_off_npv_kW', case_list_aspect2_on,
                                     'NPV per kW USD per kW ', '')
            if file == "stage1_mgs":
                costs_stage1 = costs_stage.copy()
            elif file == "stage2_mgs":
                costs_stage2 = costs_stage.copy()
            elif file == "stage3_mgs":
                costs_stage3 = costs_stage.copy()
            elif file == "no_mgs":
                costs_no_mgs = costs_stage.copy()

            costs_stage = add_statistics_matrix(costs_stage)
            for column in favoured.columns:
                costs_stage[column] = favoured[column]
            costs_stage['nesp_id'] = name_list + ['', '', '', '']
            costs = costs.append(costs_stage.drop(['min', 'max', 'average', 'sum']), sort=False)            #
            costs_stage.to_csv(folder + save_subfolder + "costs_" + file + '_' + prefix[:-1] + ".csv")

        title_favoured_columns = favoured.columns
        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect1[[name + ' global perspective' for name in case_list_aspect1]],
                     title_favoured_columns[0], ' global perspective')
        add_sum_save(folder, save_subfolder, prefix,
            number_of_favoured_aspect2_on_off[[name + ' global perspective' for name in case_list_aspect2_on_off]],
                     title_favoured_columns[1], ' global perspective')
        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect2_on[[name + ' global perspective' for name in case_list_aspect2_on]],
                     title_favoured_columns[2], ' global perspective')
        add_sum_save(folder, save_subfolder, prefix,
            number_of_favoured_aspect3_on_off[[name + ' global perspective' for name in case_list_aspect3_on_off]],
                     title_favoured_columns[3], ' global perspective')
        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect3_on[[name + ' global perspective' for name in case_list_aspect3_on]],
                     title_favoured_columns[4], ' global perspective')
        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect3_npv[[name + ' global perspective' for name in case_list_aspect3_all]],
                     title_favoured_columns[5], ' global perspective')
        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect3_lcoe[[name + ' global perspective' for name in case_list_aspect3_all]],
                     title_favoured_columns[6], ' global perspective')
        add_sum_save(folder, save_subfolder, prefix,
            number_of_favoured_aspect3_adapt_lcoe[[name + ' global perspective' for name in case_list_aspect3_adapt]],
                     title_favoured_columns[7], ' global perspective')

        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect1[[name + ' mg perspective' for name in case_list_aspect1]], name_list[0],
                     'mg perspective')
        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect2_on_off[[name + ' mg perspective' for name in case_list_aspect2_on_off]],
                     title_favoured_columns[1], ' mg perspective')
        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect2_on[[name + ' mg perspective' for name in case_list_aspect2_on]],
                     title_favoured_columns[2], ' mg perspective')
        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect3_on_off[[name + ' mg perspective' for name in case_list_aspect3_on_off]],
                     title_favoured_columns[3], ' mg perspective')
        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect3_on[[name + ' mg perspective' for name in case_list_aspect3_on]],
                     title_favoured_columns[4], ' mg perspective')
        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect3_npv[[name + ' mg perspective' for name in case_list_aspect3_all]],
                     title_favoured_columns[5], ' mg perspective')
        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect3_lcoe[[name + ' mg perspective' for name in case_list_aspect3_all]],
                     title_favoured_columns[6], ' mg perspective')
        add_sum_save(folder, save_subfolder, prefix,
            number_of_favoured_aspect3_adapt_lcoe[[name + ' mg perspective' for name in case_list_aspect3_adapt]],
                     title_favoured_columns[7], ' mg perspective')


        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect2_on_off[[name + ' mg perspective' for name in case_list_aspect2_on_off]],
                     title_favoured_columns[1], '')
        add_sum_save(folder, save_subfolder, prefix, number_of_favoured_aspect2_on[[name + ' mg perspective' for name in case_list_aspect2_on]],
                     title_favoured_columns[2], '')

        favoured = costs[[item for item in favoured.columns]]
        favoured['nesp_id']=costs['nesp_id']
        costs = costs.drop([item for item in favoured.columns], axis=1)

        costs = add_statistics_matrix(costs)
        for column in favoured.columns:
            costs[column] = favoured[column]

        costs.to_csv(folder + save_subfolder + "costs_all_solutions_" + prefix[:-1] + ".csv")

        comparison_list_y_1 = [title + ' mg perspective' for title in
                             ['LCOE USD per kWh ' + item for item in list_cases]]

        comparison_list_y_2 = [title + ' global perspective' for title in
                             ['LCOE USD per kWh ' + item for item in list_cases]]

        comparison_list_y_3 = ['LCOE USD per kWh ' + item for item in list_cases_small]

        comparison_list_x = ['Peak demand kW',
                             'Distance to national grid km',
                             'Additional branch distance km',
                             'Customers ']

        if grid_arrival == 5:

            number = plot_x_y_stages(folder, "evaluation/", prefix, comparison_list_x, comparison_list_y_3,
                                    costs_stage1, costs_stage2, costs_stage3,
                                    costs_no_mgs, number_5)

            number = plot_x_y_stages(folder, save_subfolder, prefix, comparison_list_x, comparison_list_y_1, costs_stage1, costs_stage2, costs_stage3,
                                 costs_no_mgs, number)

            number = plot_x_y_stages(folder, save_subfolder, prefix, comparison_list_x, comparison_list_y_2, costs_stage1, costs_stage2, costs_stage3,
                                 costs_no_mgs, number)

        number = plot_comparison_intercon(folder, save_subfolder, prefix, comparison_list_x, comparison_list_y_1, costs,
                                          number, 'mg perspective')

        number = plot_comparison_intercon(folder, save_subfolder, prefix, comparison_list_x, comparison_list_y_2, costs,
                                          number, 'global perspective')

        for y in comparison_list_y_1 + comparison_list_y_2 + comparison_list_y_3:
            number = plot_matrix(folder, save_subfolder, prefix, costs, number, y)

print('ATTENTION! LCOE AND NPV CORRECTION FOR DISTRIBUTION GRID ERROR IN PLACE')
save_subfolder = 'evaluation'
for grid_arrival in range(1,20):
    save_subfolder_loop = save_subfolder+"_"+str(grid_arrival)+'/'
    evaluate_grid_arrival_time(grid_arrival, save_subfolder_loop)
    print('Interconnection after ' + str(grid_arrival) + ' evaluated.')
