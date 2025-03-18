from DAL.InvoiceDAL import InvoiceDAL

invoice_dal = InvoiceDAL()
list_product = invoice_dal.get_all_invoices()
for invoice in list_product:
    print(invoice)