from typing import List

from fastapi import APIRouter, HTTPException, Depends, status, Query
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ContactModel, ContactUpdate, ContactResponse
from src.repository import contacts as repository_contacts


router = APIRouter(prefix='/contacts', tags=["contacts"])


@router.get("/find", response_model=List[ContactResponse])
async def find_contacts(firstname: str = Query(None),
                        lastname: str = Query(None),
                        email: str = Query(None),
                        db: Session = Depends(get_db)):

    contacts = await repository_contacts.find_contacts(db, firstname, lastname, email)

    if len(contacts) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found")

    return contacts


@router.get("/", response_model=List[ContactResponse])
async def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):

    contacts = await repository_contacts.get_contacts(skip, limit, db)

    if len(contacts) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found")

    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def read_contact(contact_id: int, db: Session = Depends(get_db)):

    contact = await repository_contacts.get_contact(contact_id, db)

    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")

    return contact


@router.get("/birthdays/", response_model=List[ContactResponse])
async def nearest_birthdays(days: int | None = 7, db: Session = Depends(get_db)):

    contacts = await repository_contacts.get_birthdays(days, db)

    if not len(contacts):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No birthdays found in {days} days")

    return contacts


@router.post("/", response_model=ContactResponse)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):

    return await repository_contacts.create_contact(body, db)


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(contact_id: int, body: ContactUpdate, db: Session = Depends(get_db)):

    contact = await repository_contacts.update_contact(contact_id, body, db)

    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")

    return contact


@router.delete("/{contact_id}", response_model=ContactResponse)
async def remove_contact(contact_id: int, db: Session = Depends(get_db)):

    contact = await repository_contacts.remove_contact(contact_id, db)

    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")

    return contact
