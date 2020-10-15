# -*- coding: utf-8 -*-

import sys
import pandas as pd
import numpy as np

from tsp_solver.greedy import solve_tsp

DEFAULT_CSVFILE = 'input-routes.csv'


class FindRoute:
    origin = None
    destination = None
    data = None
    all_destinations = set()

    def __init__(self, _origin, _destination, _filename=DEFAULT_CSVFILE):
        self.origin = _origin
        self.destination = _destination
        self.df = FindRoute.generate_matrix(_filename)
        self.normalize_dataframe()

    @staticmethod
    def generate_matrix(csvfilename):
        try:
            with open(csvfilename) as csvfile:
                df = pd.read_csv(csvfile, usecols=[0, 1, 2], names=['A', 'B', 'C'])
            return pd.pivot_table(df, index='A', columns='B', values='C')
        except Exception as e:
            raise

    def normalize_dataframe(self):
        rows = self.df.index
        columns = self.df.columns

        for name in rows:
            if name not in columns:
                self.df.insert(len(self.df.columns), name, np.nan)

        for name in columns:
            if name not in rows:
                self.df = self.df.append(pd.Series(name=name))

        self.df = self.df.reindex(columns=sorted(self.df.columns))
        self.df = self.df.sort_index()

    def generate_routes(self):
        mat = self.df.fillna(10000).values

        return solve_tsp(mat, endpoints=(self.get_position_by_name(self.origin),
                                         self.get_position_by_name(self.destination)))

    def sum_route_prices(self, route=[]):
        price = 0
        before = None

        for i in route:
            if before is None:
                before = i
                continue
            else:
                price += 0 if pd.isna(self.df.iloc[before][i]) else self.df.iloc[before][i]
                before = i

        return price

    def get_name_by_position(self, position):
        return self.df.columns[position]

    def get_position_by_name(self, name):
        return self.df.columns.get_loc(name)

    def main(self):
        route_index = self.generate_routes()
        price = self.sum_route_prices(route_index)
        route_names = [self.get_name_by_position(position) for position in route_index]

        return {
            'route': route_names,
            'price': price
        }


if __name__ == '__main__':
    filename = input("Enter filename csv (case None default is {}): ".format(DEFAULT_CSVFILE)) or 'input-routes.csv'
    origin = str(input("Enter origin point (required): ")).upper()
    destination = str(input("Enter destination point (required): ")).upper()

    if not origin or not destination:
        raise Exception("Origin and destination are required!")

    solution = FindRoute(origin, destination, filename)
    result = solution.main()
    print("best route: {} > $ {}".format(result.get('route', None), result.get('price', None)))
    sys.exit()
