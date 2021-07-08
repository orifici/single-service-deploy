import os
import time
import requests
from jinja2 import Environment, FileSystemLoader


class TemplateGenerator():
    """ A helper class.
        It is used to generate html output from a template
    """

    def __init__(self,
                 template_dir="templates",
                 out_dir="www",
                 out_file="index.html"):
        self.out_dir = out_dir
        self.out_file = out_file
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template('welcome.html.j2')
        self._out_dir()

    def _out_dir(self):
        """ check the output dir exists. If not, it will create it """
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)

    def render_template(self, template_data):
        """ Renders `template_data` to file """
        with open(os.path.join(self.out_dir, self.out_file), "w") as main_page:
            main_page.write(self.template.render(template_data))


class DataMiner():
    """ A class to retrieve the current bitcoin value from
        a public API
    """

    def __init__(self, endpoint, currency):
        self.endpoint = endpoint
        self.currency = currency
        self.data = {}
        self.iteration = 0
        self.prices = []

    def call_api(self):
        """ Call the API and retrieve the current price """
        json_data = requests.get(self.endpoint)
        json_resp = json_data.json()
        bpi = float(
            json_resp.get("bpi").get(self.currency).get('rate_float'))
        self.prices.append(bpi)
        self.data[f'{self.currency.lower()}_bpi'] = bpi
        self.iteration += 1
        return self


if __name__ == "__main__":
    output_generator = TemplateGenerator()
    api_handler = DataMiner(
        endpoint="https://api.coindesk.com/v1/bpi/currentprice/USD.json",
        currency="USD"
    )

    # Loop indefinitely, pause every 60 secs
    while True:
        api_handler.call_api()

        # Render the template with prices
        output_generator.render_template(template_data=api_handler.data)

        # logging. TODO: implement proper logging
        print(f'iteration: {api_handler.iteration}, \
               n_values: {len(api_handler.prices)}, \
               price: {api_handler.data["usd_bpi"]}', flush=True)
        time.sleep(60)
