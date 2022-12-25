"""Added status column

Revision ID: 9a15b4430b68
Revises: 3510cdb16c9d
Create Date: 2021-10-25 17:32:11.634881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a15b4430b68'
down_revision = '3510cdb16c9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assessments', sa.Column('status', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assessments', 'status')
    # ### end Alembic commands ###
