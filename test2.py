def menu():
    print("\n")
    print("--- 人事資料管理系統 ---")
    print("1. 新增資料")
    print("2. 查詢資料")
    print("3. 修改資料")
    print("4. 刪除資料")
    print("5. 顯示所有資料")
    print("6. 退出系統")
    print("------------------------")

def add(records):
    while True:
        department = input("請輸入部門: ")
        name = input("請輸入姓名: ")
        age = input("請輸入年齡: ")
        phone = input("請輸入手機號碼: ")
        records.append({'部門': department, '姓名': name, '年齡': age, '手機': phone})
        cont = input("是否繼續新增資料? (y/n): ")
        if cont.lower() != 'y':
            break

def query(records):
    name = input("請輸入要查詢的姓名: ")
    results = find(records, name)
    if results:
        print("--- 查詢結果 ---")
        display(results)
    else:
        print("查無此人。")

def modify(records):
    name = input("請輸入要修改的姓名: ")
    results = find(records, name)
    if results:
        print("當前資料:")
        display(results)
        record = results[0]
        print("1. 修改部門\n2. 修改姓名\n3. 修改年齡\n4. 修改手機")
        field = input("請選擇要修改的欄位: ")
        if field == '1':
            record['部門'] = input("請輸入新的部門: ")
        elif field == '2':
            record['姓名'] = input("請輸入新的姓名: ")
        elif field == '3':
            record['年齡'] = input("請輸入新的年齡: ")
        elif field == '4':
            record['手機'] = input("請輸入新的手機號碼: ")
        else:
            print("無效選項")
        print("--- 更新後的資料 ---")
        display([record])
    else:
        print("查無此人。")

def delete(records):
    name = input("請輸入要刪除的姓名: ")
    results = find(records, name)
    if results:
        record = results[0]
        print("確定要刪除 {} 的資料嗎? (y/n): ".format(record['姓名']))
        confirm = input()
        if confirm.lower() == 'y':
            records.remove(record)
            print(f"{record['姓名']} 的資料已刪除。")
            print("--- 剩餘的所有資料 ---")
            display(records)
        else:
            print("已取消刪除。")
    else:
        print("查無此人。")

def display(records):
    if not records:
        print("目前沒有任何資料")
    else:
        print(f"{'部門       '}{'姓名      '}{'年齡    '}{'手機'}")
        print("-" * 40)
        for record in records:
            print(f"{record['部門']+"     "}{record['姓名']+"     "}{record['年齡']+"     "}{record['手機']}")
        print("-" * 40)

def find(records, name):
    return [record for record in records if record['姓名'] == name]

def main():
    records = []
    while True:
        menu()
        choice = input("請選擇功能: ")
        if choice == '1':
            add(records)
        elif choice == '2':
            query(records)
        elif choice == '3':
            modify(records)
        elif choice == '4':
            delete(records)
        elif choice == '5':
            print("--- 所有資料 ---")
            display(records)
        elif choice == '6':
            print("系統已退出。")
            break
        else:
            print("無效選項，請重新選擇。")

main()
