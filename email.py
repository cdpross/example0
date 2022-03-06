import win32com.client
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'jlbarksdale22@gmail.com'
mail.Subject = 'hi'
mail.Body = 'hi'


mail.Send()