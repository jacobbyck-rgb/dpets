# Diamond Rework Playbook

An interactive guide to the Diamond Pet Foods account at WarehouseNow: Costco-refused loads that get reworked at a crossdock and redelivered.

- `diamond-playbook.html` is the built page. Open it in a browser.
- `src/playbook.html` is the page source. Data is injected at `/*DATA*/`.
- `tools/extract_data.py` pulls depots, go-to warehouses, ADW contacts, SKUs and ticket stats out of Diamond's ticket workbook.
- `tools/build.py` rebuilds the page from a fresh workbook export:

```
pip install openpyxl
python3 tools/build.py "Diamond Pet foods - Revised.xlsx"
```
