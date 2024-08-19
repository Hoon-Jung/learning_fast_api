"""empty message

Revision ID: 8734f840abe9
Revises: 1936b97d5ac2
Create Date: 2024-08-04 20:39:55.870472

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8734f840abe9'
down_revision: Union[str, None] = '1936b97d5ac2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('modified_at', sa.DateTime(), nullable=False))
    op.add_column('replies', sa.Column('modified_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('replies', 'modified_at')
    op.drop_column('post', 'modified_at')
    # ### end Alembic commands ###