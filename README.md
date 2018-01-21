# What is it

Treecount is a small website using python3 and django to manage expenses between several users.

When a group of people share expenses on a regular basis, they might want to know how much money each spends and who to refund.

**DISCLAIMER: Treecount assumes that every user is well intentioned and will not try to mess things up. Every user can edit any expense or refund**
**DISCLAIMER AGAIN: Treecount might be full of security holes. Run it on a secure/trusty network**

# Requirements

Currently, Treecount works with python3 and django 1.10.

# Installation

```
virtualenv ve
source ve/bin/activate
pip install -r requirements.lock
```

Run the server however you want (there is a `treecount.wsgi` module if you want to deploy it cleanly)

# Usage

Create a superuser using django

```
python manage.py createsuperuser
```

Add users through the admin (`mysuperdomainname.com/admin`). Users can be deactivated to not appear in the selection fields.

Expenses are the main resources. They have one creditor and several debitors and split evenly the amount spent between them.

Refunds allow to transfer money between two users.

You can check the balance and how to even it out in the last two tabs.