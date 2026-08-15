# Python - Object-Relational Mapping (ORM)

## Project Overview
This project bridges Python programming and relational databases using MySQL and SQLAlchemy. It covers raw SQL querying using `MySQLdb` (MySQL-python module) as well as modern Object-Relational Mapping (ORM) using SQLAlchemy to handle database schemas, records, and model relationships seamlessly.

## General Requirements
* **Allowed Editors:** `vi`, `vim`, `emacs`
* **Python Version:** Python 3.8.x
* **Database Driver:** `MySQLdb` (version 2.0.x)
* **ORM:** SQLAlchemy (version 1.4.x)
* **Code Style:** `pycodestyle` (version 2.8.*)
* All scripts must be executable (`chmod +x <filename>`)
* All code must strictly avoid execution when imported (`if __name__ == "__main__":`)

---

## Tasks Summary

| Task # | File Name | Description |
| :--- | :--- | :--- |
| **0** | `0-select_states.py` | Lists all `states` from database sorted by `states.id`. |
| **1** | `1-filter_states.py` | Lists states with name starting with `N` (uppercase). |
| **2** | `2-my_filter_states.py` | Displays state matching user input query. |
| **3** | `3-my_safe_filter_states.py` | Prevents SQL injection using parameterized queries. |
| **4** | `4-cities_by_state.py` | Lists all cities joined with state names. |
| **5** | `5-filter_cities.py` | Lists all cities in a given state name argument. |
| **6** | `model_state.py` | Defines `State` model class using SQLAlchemy `declarative_base()`. |
| **7** | `7-model_state_fetch_all.py` | Lists all `State` objects via SQLAlchemy session. |
| **8** | `8-model_state_fetch_first.py` | Prints first `State` object ordered by `id`. |
| **9** | `9-model_state_filter_a.py` | Filters `State` objects containing letter `a`. |
| **10** | `10-model_state_my_get.py` | Prints `State` ID matching target name safely. |
| **11** | `11-model_state_insert.py` | Inserts `State` object "Louisiana" into DB. |
| **12** | `12-model_state_update_id_2.py` | Updates `State` record where `id = 2` to "New Mexico". |
| **13** | `13-model_state_delete_a.py` | Deletes all states containing letter `a`. |
| **14** | `model_city.py`, `14-model_city_fetch_by_state.py` | Defines `City` class model and lists city objects. |
| **15** | `relationship_city.py`, `relationship_state.py`, `100-relationship_states_cities.py` | Establishes ORM cascade relationship between state and city models. |
| **16** | `101-relationship_states_cities_list.py` | Queries states and linked cities via single ORM query. |
| **17** | `102-relationship_cities_states_list.py` | Queries cities and accesses parent `State` model via relationship backref. |

---

## Author
* **Ishimwe12-ALT**
