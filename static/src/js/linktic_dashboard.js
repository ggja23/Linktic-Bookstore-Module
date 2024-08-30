/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";

const actionRegistry = registry.category("actions");

class LinkticDashboard extends Component {
    setup() {
        super.setup();
        this.orm = useService('orm');
        this._fetchData();
    }

    _fetchData() {
        this.orm.call("linktic.sale.order", "get_dashboard_data", [], {}).then(result => {
            document.getElementById('total_sales_data').innerHTML = result.total_sales;
            document.getElementById('total_products_sold_data').innerHTML = result.total_products_sold;
            document.getElementById('stock_levels_data').innerHTML = result.stock_levels;
            document.getElementById('recent_sales_data').innerHTML = result.recent_sales;
        });
    }
}

LinkticDashboard.template = "linktic_dashboard_template";
actionRegistry.add("linktic_dashboard_tag", LinkticDashboard);
