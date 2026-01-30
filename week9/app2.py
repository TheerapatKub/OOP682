"""app2.py
Simple OOP people manager (Student / Staff) with a small CLI and basic tests.

Usage:
  python app2.py            # run interactive CLI
  python app2.py --test     # run basic built-in tests
"""
from __future__ import annotations
import json
import sys
from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class Person:
    pid: str
    name: str
    age: int

    def __str__(self) -> str:
        return f"{self.name} ({self.pid}) - {self.age} years"


@dataclass
class Student(Person):
    student_id: str

    def __str__(self) -> str:
        return f"Student: {super().__str__()}, Student ID: {self.student_id}"


@dataclass
class Staff(Person):
    staff_id: str

    def __str__(self) -> str:
        return f"Staff: {super().__str__()}, Staff ID: {self.staff_id}"


class PeopleRepo:
    """In-memory repository with optional JSON save/load"""

    def __init__(self) -> None:
        self._people: List[Person] = []

    def add(self, p: Person) -> None:
        if self.find_by_pid(p.pid) is not None:
            raise ValueError("pid already exists")
        self._people.append(p)

    def list_all(self) -> List[Person]:
        return list(self._people)

    def find_by_pid(self, pid: str) -> Optional[Person]:
        for p in self._people:
            if p.pid == pid:
                return p
        return None

    def save(self, path: str) -> None:
        serialized = []
        for p in self._people:
            d = asdict(p)
            d["__class__"] = p.__class__.__name__
            serialized.append(d)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(serialized, f, indent=2, ensure_ascii=False)

    def load(self, path: str) -> None:
        with open(path, "r", encoding="utf-8") as f:
            items = json.load(f)
        self._people = []
        for d in items:
            cls = d.pop("__class__", "Person")
            if cls == "Student":
                self._people.append(Student(**d))
            elif cls == "Staff":
                self._people.append(Staff(**d))
            else:
                self._people.append(Person(**d))


def interactive_loop(repo: PeopleRepo) -> None:
    menu = (
        "\nSimple People Manager:\n"
        "1) Add Student\n"
        "2) Add Staff\n"
        "3) List all\n"
        "4) Find by PID\n"
        "5) Save to JSON\n"
        "6) Load from JSON\n"
        "0) Exit\n"
    )
    while True:
        print(menu)
        choice = input("Choose: ").strip()
        if choice == "1":
            pid = input("PID: ").strip()
            name = input("Name: ").strip()
            age = int(input("Age: ").strip())
            sid = input("Student ID: ").strip()
            try:
                repo.add(Student(pid, name, age, sid))
                print("Student added.")
            except ValueError as e:
                print("Error:", e)
        elif choice == "2":
            pid = input("PID: ").strip()
            name = input("Name: ").strip()
            age = int(input("Age: ").strip())
            stf = input("Staff ID: ").strip()
            try:
                repo.add(Staff(pid, name, age, stf))
                print("Staff added.")
            except ValueError as e:
                print("Error:", e)
        elif choice == "3":
            for p in repo.list_all():
                print(" -", p)
        elif choice == "4":
            pid = input("Search PID: ").strip()
            p = repo.find_by_pid(pid)
            if p:
                print(p)
            else:
                print("Not found")
        elif choice == "5":
            path = input("Path to save (e.g. people.json): ").strip()
            repo.save(path)
            print("Saved.")
        elif choice == "6":
            path = input("Path to load (e.g. people.json): ").strip()
            repo.load(path)
            print("Loaded.")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def run_tests() -> None:
    repo = PeopleRepo()
    s = Student("123", "Alice", 20, "S-001")
    t = Staff("456", "Bob", 35, "ST-01")
    repo.add(s)
    repo.add(t)
    assert repo.find_by_pid("123") is s
    assert repo.find_by_pid("456") is t
    fn = "_test_people.json"
    repo.save(fn)
    repo2 = PeopleRepo()
    repo2.load(fn)
    assert any(isinstance(x, Student) and x.pid == "123" for x in repo2.list_all())
    assert any(isinstance(x, Staff) and x.pid == "456" for x in repo2.list_all())
    print("All tests passed")


def main(argv: List[str] = None) -> None:
    argv = argv or sys.argv[1:]
    repo = PeopleRepo()
    if argv and argv[0] == "--test":
        run_tests()
        return
    print("Starting interactive People Manager. Use --test to run built-in tests.")
    interactive_loop(repo)


if __name__ == "__main__":
    main()
