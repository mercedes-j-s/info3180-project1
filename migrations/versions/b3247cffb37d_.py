"""empty message

Revision ID: b3247cffb37d
Revises: 
Create Date: 2022-03-18 21:29:54.700659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3247cffb37d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('bedrooms', sa.String(length=10), nullable=True),
    sa.Column('bathrooms', sa.String(length=10), nullable=True),
    sa.Column('price', sa.String(length=30), nullable=True),
    sa.Column('p_type', sa.String(length=20), nullable=True),
    sa.Column('location', sa.String(length=200), nullable=True),
    sa.Column('photo', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('location')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property')
    # ### end Alembic commands ###
