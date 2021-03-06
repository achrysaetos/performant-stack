"""Add username and password

Revision ID: a7c7ce11791b
Revises: 61dd58bdc80f
Create Date: 2022-06-12 16:17:19.692045

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a7c7ce11791b'
down_revision = '61dd58bdc80f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('password', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'users', ['username'])
    op.drop_column('users', 'role')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', postgresql.ENUM('teacher', 'student', name='role'), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'password')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
